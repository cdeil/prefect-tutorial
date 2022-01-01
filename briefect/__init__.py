"""A minimal re-implementation of parts of Prefect from scratch.

This is a learning exercise, in real life use Prefect.

TODO:
* logger on context
* data flow tracing to build DAG
* code to execute flow
* exception handling and errors
* Implement State
* Implement FlowRunner
* Implement TaskRunner
* Implement LocalExecutor
"""

__all__ = [
    "Task",
    "task",
    "Flow",
    "context",
]

from .context import context
from .task import Task, task
from .flow import Flow
