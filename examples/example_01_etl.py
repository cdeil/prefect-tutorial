"""Prefect example with `task` and `Flow` basics.

A task is a Python function under Prefect supervision.
A flow is a workflow DAG under Prefect supervision.
Typically, flows are ETL, i.e. they start by extracting
the data from somewhere and end by storing it somewhere.
It is not super common but possible to access task or flow
return values from `state = flow.run()`.
"""
from prefect import task, Flow, Parameter


@task
def extract():
    print("running extract")
    return 40


@task
def transform(val, plus):
    print(f"running transform with {val=} and {plus=}")
    return val + plus


@task
def load(result):
    print(f"running load with {result=}")


print("Creating flow DAG")
with Flow("My ETL") as my_etl:
    p = Parameter("p", default=2)
    x = extract()
    y = transform(x, p)
    load(y)

# my_etl.visualize()

print("Execute flow")
state = my_etl.run()

print("All done. State and results:")
print(f"{state.result[y].result=}")
