"""Example for minprefect."""
from prefect import task, Flow

from briefect import task, Flow


@task
def extract():
    print("running extract")
    return 42


@task
def transform(data):
    print("running transform")
    return data + 1


@task
def load(data):
    print(f"Loading data: {data}")


print("create flow")
with Flow("My ETL") as my_etl:
    print("start flow definition")
    print(f"my_etl: {my_etl}")
    x = extract()
    print(f"x: {x}")
    y = transform(x)
    print(f"y: {y}")
    z = load(y)
    print(f"z: {z}")
    print("end flow definition")

print(f"my_etl: {my_etl}")

# my_etl.visualize()

state = my_etl.run()
print(f"state: {state}")
print(f"type(state): {type(state)}")
print(f"result: {state.result}")
print(f"type(state.result): {type(state.result)}")
