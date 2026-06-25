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
                        try:
                            experience = agent.execute(step)
                            self.experiences.append(experience)
                        except Exception as e:
                            # Handle agent execution errors
                            logger.error(f"Error executing agent {agent.id}: {e}")
                            raise AgentError(f"Error executing agent {agent.id}: {e}")

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
                    try:
                        experience = agent.execute(step)
                        logger.info(f"Agent experience: {experience}")
                    except Exception as e:
                        # Handle agent execution errors in debug mode
                        logger.error(f"Error executing agent {agent.id} in debug mode: {e}")