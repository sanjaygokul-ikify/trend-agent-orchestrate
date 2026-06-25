from typing import List, Dict, Optional
from logging import getLogger
from .types import Workflow, Agent, Experience
from .exceptions import OrchestrationError

logger = getLogger(__name__)

class Engine:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow
        self.agents: Dict[str, Agent] = {}
        self.experiences: List[Experience] = []

    def execute(self) -> List[Experience]:
        try:
            # Initialize agents
            for agent in self.workflow.agents:
                self.agents[agent.id] = agent

            # Run workflow loops
            for step in self.workflow.steps:
                # Trigger agents
                for agent in self.agents.values():
                    if agent.trigger(step):
                        # Execute agent actions
                        experience = agent.execute(step)
                        self.experiences.append(experience)

            # Return experiences
            return self.experiences
        except Exception as e:
            # Log and re-raise exceptions
            logger.error(f"Error executing workflow: {e}")
            raise OrchestrationError(f"Error executing workflow: {e}")

    def debug(self):
        # Log workflow execution
        logger.info(f"Executing workflow: {self.workflow.id}")
        for step in self.workflow.steps:
            logger.info(f"Executing step: {step.id}")
            for agent in self.agents.values():
                if agent.trigger(step):
                    logger.info(f"Triggering agent: {agent.id}")
                    experience = agent.execute(step)
                    logger.info(f"Agent experience: {experience}")
