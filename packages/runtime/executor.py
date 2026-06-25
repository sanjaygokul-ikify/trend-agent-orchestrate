from logging import getLogger
from packages.core.engine import Engine
from packages.core.types import Workflow

logger = getLogger(__name__)

class Executor:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow
        self.engine = Engine(workflow)

    def run(self):
        try:
            # Execute workflow
            experiences = self.engine.execute()
            # Log and return experiences
            logger.info(f"Experiences: {experiences}")
            return experiences
        except Exception as e:
            # Log and re-raise exceptions
            logger.error(f"Error executing workflow: {e}")
            raise
