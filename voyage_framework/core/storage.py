
from __future__ import annotations
import json, threading, shutil
from pathlib import Path
from typing import Any

_LOCK=threading.Lock()

def atomic_write(path:Path, content:str)->None:
    path=Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(content, encoding='utf-8')
    tmp.replace(path)

def append_entry(path:Path, content:str, frontmatter:dict[str,Any])->None:
    path=Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    block=f"---\n{json.dumps(frontmatter)}\n---\n{content}\n"
    with _LOCK:
        with open(path,'a',encoding='utf-8') as f:
            f.write(block)

def parse_frontmatter_entries(path:Path):
    path=Path(path)
    if not path.exists():
        return []
    txt=path.read_text(encoding='utf-8')
    chunks=[c for c in txt.split('---\n') if c.strip()]
    out=[]
    for i in range(0,len(chunks),2):
        try:
            fm=json.loads(chunks[i].strip())
            content=chunks[i+1].strip()
            out.append({'frontmatter':fm,'content':content})
        except Exception:
            continue
    return out

def append_jsonl(path:Path,data:dict[str,Any])->None:
    path=Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _LOCK:
        with open(path,'a',encoding='utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False,default=str)+"\n")

def load_jsonl(path:Path):
    path=Path(path)
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def journal_rotate(path:Path,max_size_bytes:int=1024*1024,max_files:int=3):
    path=Path(path)
    if not path.exists() or path.stat().st_size<max_size_bytes:
        return
    for i in range(max_files,0,-1):
        p=Path(f"{path}.{i}")
        if p.exists():
            if i==max_files:
                p.unlink()
            else:
                p.rename(Path(f"{path}.{i+1}"))
    shutil.move(path, Path(f"{path}.1"))
