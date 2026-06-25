from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    id: str
    trigger: callable
    execute: callable

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
