"""Prefect example for imperative API with `Task` and `Flow`.

Mostly Prefect is used via the "functional" API that we saw in the previous example.
The imperative API can be useful to declare state dependencies without data dependencies
and for more fine-grained control. We show it here this early mainly since it
is much simpler to see and understand how a flow DAG is created.

https://docs.prefect.io/core/concepts/flows.html#imperative-api
"""
from prefect import Task, Flow


class Extract(Task):
    def run(self):
        print("running Extract.run")
        return 42


class Transform(Task):
    def run(self, val):
        print(f"running Transform.run with {val=}")
        return val + 1


class Load(Task):
    def run(self, result):
        print(f"running Load.run with {result=}")


print("Creating task objects")
extract = Extract()
transform = Transform()
load = Load()

print("Creating flow DAG consisting of task objects")
flow = Flow("My Imperative Flow")
# TODO: is it possible to define data dependencies with this API?
flow.set_dependencies(
    task=transform, upstream_tasks=[extract], keyword_tasks={"val": 10}
)
flow.set_dependencies(
    task=load, upstream_tasks=[transform], keyword_tasks={"result": 10}
)

flow.visualize()
flow.run()
