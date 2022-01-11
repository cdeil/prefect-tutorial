"""Prefect scheduling examples.

Example from here: https://docs.prefect.io/core/concepts/schedules.html
"""
from prefect import task, Flow
import datetime
import pandas as pd
from prefect.schedules import IntervalSchedule


@task
def say_hello():
    print("Hello, world!")


# Schedules work with either datetime or pandas, the following two are equivalent
schedule = IntervalSchedule(
    start_date=pd.Timestamp.now(tz="utc"),
    interval=pd.Timedelta("10s"),
)
schedule = IntervalSchedule(
    start_date=datetime.datetime.utcnow(),
    interval=datetime.timedelta(seconds=10),
)

print(f"{schedule.start_date=}")
print(f"{schedule.next(2)=}")

with Flow("Hello", schedule) as flow:
    say_hello()

flow.run()
