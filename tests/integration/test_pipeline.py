import unittest
from packages.core.engine import Engine
from packages.core.types import Workflow, Agent, Experience

class TestPipeline(unittest.TestCase):
    def test_pipeline_execution(self):
        workflow = Workflow(
            id='example-workflow',
            agents=[
                Agent(
                    id='example-agent',
                    trigger=lambda step: True,
                    execute=lambda step: Experience(
                        agent_id='example-agent',
                        step_id='example-step',
                        outcome='success'
                    )
                )
            ],
            steps=[
                Step(
                    id='example-step',
                    actions=['example-action']
                )
            ]
        )
        engine = Engine(workflow)
        experiences = engine.execute()
        self.assertEqual(len(experiences), 1)