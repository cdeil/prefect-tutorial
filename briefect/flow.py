from .context import context


class Flow:
    """A Flow is a set of tasks and edges representing dependencies.

    DAG = directed acyclic graph

    We implement the two ways ("functional", "imperative") to create a flow:
    https://docs.prefect.io/core/concepts/flows.html
    """

    def __init__(self, name):
        self.name = name
        self.tasks = set()
        self.edges = set()

    def __enter__(self):
        """Set this flow as active in the global context."""
        context.flow = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove this flow from active status in the global context."""
        context.flow = None

    def set_dependencies(self):
        raise NotImplementedError()

    def run(self):
        """Execute flow on data."""
        # TODO: which class decides on order of task execution? Runner? Executor?
