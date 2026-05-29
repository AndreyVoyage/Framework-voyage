
from __future__ import annotations
import json
from pathlib import Path
from pydantic import BaseModel, Field
from voyage_framework.core.models import Event, EventType
from voyage_framework.core.storage import atomic_write

class TaskSpec(BaseModel):
    role:str
    task:str
    micro_phase:str='M1'
    project_id:str='default'
    criteria:list[str]=Field(default_factory=lambda:['Run pytest','Run mypy'])
    context_json:dict={}
    task_markdown:str

class TaskGenerator:
    def __init__(self, engine):
        self.engine=engine

    def generate(self, role:str, task:str, micro_phase:str='M1', project_id:str='default')->TaskSpec:
        md=f"# TASK\n\nRole: {role}\nTask: {task}\n"
        spec=TaskSpec(role=role,task=task,micro_phase=micro_phase,project_id=project_id,context_json={'role':role},task_markdown=md)
        self.engine.append(Event(event_type=EventType.PLAN_CREATED,payload={'task':task},project_id=project_id))
        return spec

    def write_task_files(self,spec:TaskSpec,task_path:Path,context_path:Path):
        atomic_write(task_path,spec.task_markdown)
        atomic_write(context_path,json.dumps(spec.context_json))
        return task_path, context_path
