class Edge:
    """Edge is a connection between tasks."""

    def __init__(self, upstream_task, downstream_task, key: str = None):
        self.upstream_task = upstream_task
        self.downstream_task = downstream_task
        self.key = key
