from packages.core.types import Workflow, Agent, Experience
from packages.core.exceptions import OrchestrationError
from packages.core.engine import Engine

class OrchestratorService:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow
        self.engine = Engine(workflow)

    def execute(self) -> List[Experience]:
        try:
            return self.engine.execute()
        except OrchestrationError as e:
            raise e