class OrchestrationError(Exception):
    pass

class AgentError(OrchestrationError):
    pass

class WorkflowError(OrchestrationError):
    pass
