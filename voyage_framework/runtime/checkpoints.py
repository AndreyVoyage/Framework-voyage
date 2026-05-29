
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

class CheckpointStore:
    def __init__(self, root: Path | str = '.voyage/checkpoints'):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, checkpoint_id:str, state:dict[str, Any]):
        (self.root / f'{checkpoint_id}.json').write_text(json.dumps(state, ensure_ascii=False, indent=2, default=str), encoding='utf-8')

    def load(self, checkpoint_id:str):
        path=self.root / f'{checkpoint_id}.json'
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding='utf-8'))
