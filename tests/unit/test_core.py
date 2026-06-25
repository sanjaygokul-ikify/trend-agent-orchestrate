import unittest
from packages.core.engine import Engine
from packages.core.types import Workflow, Agent, Experience

class TestCore(unittest.TestCase):
    def test_engine_init(self):
        workflow = Workflow(
            id='example-workflow',
            agents=[],
            steps=[]
        )
        engine = Engine(workflow)
        self.assertIsNotNone(engine)

    def test_engine_execute(self):
        workflow = Workflow(
            id='example-workflow',
            agents=[],
            steps=[]
        )
        engine = Engine(workflow)
        experiences = engine.execute()
        self.assertEqual(experiences, [])