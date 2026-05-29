from __future__ import annotations

import json, sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from voyage_framework.core.models import Event, EventType
from voyage_framework.core.storage import append_jsonl, journal_rotate

class EventEngine:
    def __init__(self, db_path: Path|str='.voyage/events.db', jsonl_path: Path|str='.voyage/events.jsonl'):
        self.db_path = Path(db_path)
        self.jsonl_path = Path(jsonl_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('PRAGMA journal_mode=WAL;')
        conn.execute('PRAGMA foreign_keys=ON;')
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_db(self):
        with self._conn() as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY,event_type TEXT,payload TEXT,timestamp TEXT,project_id TEXT,correlation_id TEXT,agent_id TEXT,role TEXT)')
            conn.execute('CREATE INDEX IF NOT EXISTS idx_events_project ON events(project_id,timestamp)')

    def append(self, event: Event) -> Event:
        with self._conn() as conn:
            conn.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?)', (
                event.event_id,
                event.event_type.value,
                json.dumps(event.payload, ensure_ascii=False),
                event.timestamp.isoformat(),
                event.project_id,
                event.correlation_id,
                event.agent_id,
                event.role,
            ))
        append_jsonl(self.jsonl_path, event.model_dump(mode='json'))
        journal_rotate(self.jsonl_path)
        return event

    def get_events(self, project_id: Optional[str]=None, limit:int=100):
        q='SELECT * FROM events'
        params=[]
        if project_id:
            q+=' WHERE project_id=?'
            params.append(project_id)
        q+=' ORDER BY timestamp DESC LIMIT ?'
        params.append(limit)
        with self._conn() as conn:
            rows=conn.execute(q, params).fetchall()
        out=[]
        for r in rows:
            out.append(Event(event_id=r[0],event_type=EventType(r[1]),payload=json.loads(r[2]),timestamp=datetime.fromisoformat(r[3]),project_id=r[4],correlation_id=r[5],agent_id=r[6],role=r[7]))
        return out

    def get_project_context(self, project_id:str)->dict[str,Any]:
        events=self.get_events(project_id,1000)
        return {'project_id': project_id, 'total_events': len(events), 'rules_added': []}
