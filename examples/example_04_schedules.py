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


# Schedules work with either datetime or pandas
# Mixing the two doesn't work
schedule = IntervalSchedule(
    start_date=pd.Timestamp.now(),
    interval=pd.Timedelta("10s"),
)
schedule = IntervalSchedule(
    start_date=datetime.datetime.now(),
    interval=datetime.timedelta(seconds=10),
)

with Flow("Hello", schedule) as flow:
    say_hello()

flow.run()
