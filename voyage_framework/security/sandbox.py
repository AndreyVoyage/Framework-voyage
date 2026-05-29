
from __future__ import annotations
import asyncio
from pathlib import Path
from voyage_framework.core.models import SecurityLevel, SecurityPolicy, ToolResult

class SandboxBackend: ...

class DockerBackend(SandboxBackend): ...

class SubprocessBackend(SandboxBackend): ...

class SecureExecutor:
    def __init__(self, policy:SecurityPolicy, project_root:Path|None=None):
        self.policy=policy
        self.project_root=project_root or Path('.')

    def classify(self, cmd:list[str])->SecurityLevel:
        s=' '.join(cmd)
        if 'rm -rf /' in s:
            return SecurityLevel.DANGEROUS
        if cmd and cmd[0]=='rm':
            return SecurityLevel.CAUTION
        return SecurityLevel.SAFE

    async def execute(self, cmd:list[str])->ToolResult:
        if not cmd:
            return ToolResult(success=False, blocked=True, stderr='empty command')
        if cmd[0] not in self.policy.allowed_commands:
            return ToolResult(success=False, blocked=True, stderr='command not allowed')
        if self.classify(cmd)==SecurityLevel.DANGEROUS:
            return ToolResult(success=False, blocked=True, stderr='dangerous command')
        proc=await asyncio.create_subprocess_exec(*cmd,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE,cwd=self.project_root)
        out,err=await asyncio.wait_for(proc.communicate(),timeout=10)
        return ToolResult(success=proc.returncode==0,stdout=out.decode(),stderr=err.decode(),blocked=False)
