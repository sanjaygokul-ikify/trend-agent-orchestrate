from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Agent:
    id: str
    trigger: Callable[[object], bool]
    execute: Callable[[object], Experience]

@dataclass
class Experience:
    agent_id: str
    step_id: str
    outcome: str

@dataclass
class Step:
    id: str
    actions: List[str]

@dataclass
class Workflow:
    id: str
    agents: List[Agent]
    steps: List[Step]
