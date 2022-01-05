"""Prefect example for error handling.

Take the `example_01_etl.py`, make tasks fail and see what happens.
"""
from prefect import task, Flow, Parameter


@task
def extract():
    print("running extract")
    return 40


@task
def transform(val, plus):
    print(f"running transform with {val=} and {plus=}")
    raise RuntimeError("oh no")
    # import ctypes;ctypes.string_at(0) # Create a segfault
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

print("Execute flow")
state = my_etl.run()

print("All done. State and results:")
print(f"{state.result[y].result=}")
