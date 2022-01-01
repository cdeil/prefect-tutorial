import inspect
from .context import context
from .edge import Edge


class Task:
    """A task is a function under Prefect supervision"""

    def __init__(self, name: str = None):
        self.name = name

    def run(self):
        """"""
        pass

    # TODO: support *args here as well? How to infer the name?
    def __call__(self, **kwargs):
        """Calling a task adds it to the DAG"""
        flow = context.flow

        # TODO: need to make a copy of self?
        # Prefect does this, needed in minimal implementation?

        flow.tasks.add(self)

        # TODO: create edges to all upstream tasks by inspecting arguments
        # TODO: merge args and kwargs into dict that has {key: task} pairs
        key = inspect.get_arguments(self.fn)
        upstream_tasks = []
        for upstream_task in upstream_tasks:
            edge = Edge(upstream_task=upstream_task, downstream_task=self, key=key)
            flow.edges.add(edge)

        # Returning self here is key to make data flow work
        # x = task1(); task2(x)
        return self


class FunctionTask(Task):
    """Generate Task.run method from function."""

    def __init__(self, fn):
        # Set wrapped `fn` as `self.run`
        def run(obj, **kwargs):
            return fn(**kwargs)

        self.run = run


def task(fn):
    """Task function decorator.

    Creates a `Task`
    """
    return FunctionTask(fn=fn)
