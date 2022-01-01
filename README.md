# Python Prefect tutorial

A Python [Prefect](https://www.prefect.io/) workflow orchestration tutorial.

It is at a beginner to intermediate level. There are many things in Prefect that we only cover briefly (e.g.
schedules, logging, runners, server, ui, cloud, dask) or not at all (e.g. distributed computation). It should take
roughly an hour to read through the content, or two hours if you want to follow along and hack a bit with the examples.

Written by Christoph Deil in January 2022.

Feedback and contributions are welcome any time via Github issues or pull request.

## Agenda

This tutorial will use Prefect 0.15 and we will cover the following topics:

1. [Tutorial setup](#tutorial-setup)
2. [What is Prefect?](#what-is-prefect)
3. [Prefect examples](#prefect-examples)
4. [Prefect from scratch](#prefect-from-scratch)
5. [Prefect orchestration](#prefect-orchestration)
6. [Prefect Orion](#prefect-orion) 
7. [Further resources](#further-resources)

## Tutorial setup

This tutorial uses Python 3.9 and Prefect 0.15. Other versions might or might not work the same. 

If you'd like to follow along with the tutorial, one way to get the relevant code is this:

```
conda create -n prefect-tutorial python=3.9 anaconda
conda activate prefect-tutorial
pip install "prefect[viz]==0.15"
```

To check that your installation was successful and which `python` and `prefect` you're using and what their versions are:
```
% which python
% python --version
% which prefect
% prefect version
```

To execute the examples from this tutorial:
```
git clone https://github.com/cdeil/prefect-tutorial.git
cd prefect-tutorial
```

To read the code or tests or examples in the Prefect repository:
```
git clone https://github.com/PrefectHQ/prefect.git
cd prefect
```

## What is Prefect?

* Prefect is a Python workflow orchestration system. That's very vague. This tutorial should give you a better understanding of what Prefect actually does.
* Tag-line from https://www.prefect.io/: "Orchestrate the
modern data stack. The easiest way to build, run, and monitor data pipelines at scale."
* [Prefect](https://en.wikipedia.org/wiki/Prefect) is a title similar to manager. There's also [Ford Prefect](https://en.wikipedia.org/wiki/Ford_Prefect_(character)) from hitchhikers guide to the Galaxy, which seems to be a favourite book of the Prefect team, e.g. they have written a Prefect workflow called Marvin that runs their standups, named after Marvin the Paranoid Android (see [blog post](https://medium.com/the-prefect-blog/prefect-runs-on-prefect-3e6df553c3a4)).
* Prefect core - open source Python package, `prefect` cli, UI, server
  * [prefect](https://github.com/PrefectHQ/prefect) - Python package. Currently version 0.15, release 1.0 coming soon
  * [server](https://github.com/PrefectHQ/server) - Prefect API and backend
  * [ui](https://github.com/PrefectHQ/ui) - Web user interface
* Prefect cloud - cloud SaaS with hybrid execution model
  * Hybrid execution model: no code or data sent to Prefect cloud, only task and flow metadata (see e.g. [blog post](https://medium.com/the-prefect-blog/the-prefect-hybrid-model-1b70c7fd296)) 
  * SaaS for server, UI, API, scheduler
  * Does NOT offer compute and agents - have to buy (e.g. Coiled or AKS) or self-host separately 
  * Various enterprise features, security, access control, ...
  * Not sure, but I think self-hosting the server is difficult because the open-source version doesn't offer any auth?
  * See https://www.prefect.io/pricing/ - pay per successful task run (20k/month free runs, then < $0.005, misc discounts)
* Prefect Orion - Prefect 2.0 in tech preview now, with planned release in early 2022 (see section below)
* Prefect can use [Dask](https://dask.org/) to scale compute up or out when needed
* Development started in 2017 by Jeremiah Lowin, open-sourced in 2019 (see [blog post](https://medium.com/the-prefect-blog/open-sourcing-the-prefect-platform-d19a6d6f6dad))
* Developed by start-up Prefect Technologies Inc (mostly in Washington DC, now fully remote) that got $11M series A and $32M series B funding in 2021 (see [blog post](https://www.prefect.io/blog/escape-velocity)), with community contributions on Github.
* Prefect [license](https://github.com/PrefectHQ/prefect/blob/master/LICENSE) is Apache 2 (fully open source) or in parts (server, UI, Orion) [Prefect community license](https://www.prefect.io/legal/prefect-community-license/) which is not an [OSI](https://opensource.org/) approved open source license, but for most users places no significant restrictions - it basically forbids anyone except Prefect Industries Inc (e.g. AWS or Azure) to offer a competing cloud service built on Prefect (see e.g. [here](https://medium.com/the-prefect-blog/open-sourcing-the-prefect-platform-d19a6d6f6dad))    
* Very active Slack (10k members, response typically within the hour)
* Docs are pretty good. Some parts (e.g. [About Prefect - Why not airflow?](https://docs.prefect.io/core/about_prefect/why-not-airflow.html)) very wordy and long read but still not explaining fully technically how Prefect works.
* Code is pure Python and pretty good (see [Github](https://github.com/PrefectHQ/prefect)). Sometimes time is better spent reading the code than the docs, e.g. to figure out how schedulers trigger flow runs. But also easy to get lost in levels of indirection, e.g. stepping through Prefect code execution in debugger even for very simple scripts it's very difficult to follow what's going on.
* Tests are pretty good (see e.g. [tests/core/test_flow.py](https://github.com/PrefectHQ/prefect/blob/master/tests/core/test_flow.py)). Reading tests is also a good way to learn Prefect in-depth.

## Prefect examples

The Prefect core API is documented here: https://docs.prefect.io/core/

Most important parts of the API that we'll learn: `prefect.Flow`, `prefect.task` decorator, `prefect.Task`,
`prefect.Parameter`, `prefect.schedules.IntervalSchedule`.

Some more rarely used parts of the API (in our codebase) that we'll also look at: `Task.map`, `prefect.case`,
`prefect.unmapped`, `prefect.tasks.control_flow.conditional.ifelse`, `prefect.tasks.core.operators.GetItem`,
`prefect.tasks.control_flow.merge`, `prefect.context`.

Let's learn by running a few [examples](examples).

* TBD: Dask example?
* TBD: Jupyter and IPython usage examples

## Prefect from scratch

NotImplementedError: please skip this section for now, since it's very much WIP and not in a useful state yet.

Would you like to understand fully how Prefect works?

Let's re-implement a minimal simplified version of Prefect from scratch to see how e.g. `task` and `Flow` work.
For sure it is very far from complete, only a very minimal core subset of Prefect is re-implemented. This is a learning
exercise, in any real project you should use Prefect directly, not `briefect`. Also it might not be fully correct,
i.e. it could be that Prefect actually does things differently internally.

See the [briefect](briefect) Python package and try it out via [examples/example_briefect.py](examples/example_briefect.py):
```
python example/example_briefect.py
```

Notes:
* TBD: explain implementation a bit

## Prefect orchestration

So far we have been running Prefect via `flow.run()` on a single machine.
Compared to only using Python directly this makes a few things easier, mostly scheduling and error handling. 

However, Prefect was designed from the start as a workflow automation system consisting of multiple
components (api server, database, user interface, agents) that together allow managing tasks and flows
in a well-thought out way, possibly at large scale with Dask or other executors.

See https://docs.prefect.io/orchestration/ and the [architecture
overview](https://docs.prefect.io/orchestration/#architecture-overview)

We won't go in depth on this part of Prefect because (a) we don't use it yet and (b) it will significantly
change soon with Prefect Orion (see below) where the server and UI are packaged with the Python API.

But let's try out a simple example at https://cloud.prefect.io/ (see https://cloud.prefect.io/tutorial) to see what it's
about.

## Prefect Orion

Prefect Orion is the name for the new Prefect 2.0 that is in tech preview now, with planned release in early 2022.

If you'd like to learn more, read the [intro blog post](https://www.prefect.io/blog/announcing-prefect-orion/)
and check out the [website](https://www.prefect.io/orion/) and [docs](https://orion-docs.prefect.io/).

Prefect Orion will have a few significant changes, most prominently:

1. Ding, dong the DAG is dead, the wicked DAG is dead (see [song](https://youtu.be/kPIdRJlzERo))
2. Prefect embraces Python type hints as part of the API (see [here](https://orion-docs.prefect.io/concepts/flows/)
3. The Prefect server and UI are now included in the Python package (see [docs](https://orion-docs.prefect.io/tutorials/orion/))

Well, the DAG isn't really dead. The `with Flow() as flow` is dead, there's now a `@flow`
decorator. Flows are functions that call tasks at run time. So no more in-advance flow definition that creates a DAG.
Tasks are executed at runtime and the DAG is formed dynamically and then only available after for visualisation and
inspection post-run. This allows a free mix of Python normal code (if, for, while, whatever) and Prefect tasks.

Type hints are used via [Pydantic](https://pydantic-docs.helpmanual.io/) under the hood and partly it surfaces in the
API. The Prefect CLI is now built with [Typer](https://typer.tiangolo.com/), Prefect Core CLI was built with
[click](https://click.palletsprojects.com/).

The source code is available in the branch [orion on github](https://github.com/PrefectHQ/prefect/tree/orion)
and (at the time of writing) pre-release `2.0a6` is up on [pypi](https://pypi.org/project/prefect/#history).

Let's try out one quick example ([examples/example_orion.py](examples/example_orion.py)):

```
pip install -U "prefect>=2.0.0a"
prefect version
python examples/example_orion.py
```

The Prefect server and UI are now included, so you can run this locally:
```
prefect orion start
open http://localhost:4200
```

By default Prefect will now use a local SQLite database (see [here](https://orion-docs.prefect.io/tutorials/orion/#the-database))
which you can inspect to learn about the underlying data model and see what information it collects:

```
% sqlite3 ~/.prefect/orion.db 
SQLite version 3.37.0 2021-11-27 14:13:22
Enter ".help" for usage hints.
sqlite> .tables
deployment            flow_run_state        task_run_state      
flow                  saved_search          task_run_state_cache
flow_run              task_run            
sqlite> select * from flow;
75775846-911d-40ee-9909-d0767d543d00|2022-01-04 20:19:07.789835|2022-01-04 20:19:07.789852|Github Stars|[]
sqlite> select * from flow_run;
044c3280-827b-4fe9-ab91-15474a8d8526|2022-01-04 20:19:07.827114|2022-01-04 20:19:08.629000|chubby-earthworm|COMPLETED|1|2022-01-04 20:19:07.817840||2022-01-04 20:19:07.843549|2022-01-04 20:19:08.564030|1970-01-01 00:00:00.720481|891142a92d8eada2da7a118a36036e30|{"repos": ["PrefectHQ/Prefect", "PrefectHQ/miter-design"]}||{}|{}|{}|[]|0|75775846-911d-40ee-9909-d0767d543d00|||4ce19c39-7177-40fb-b2c0-ff7967f9bb8b
sqlite> select * from task_run;
a62b6e6c-86cb-4805-9614-d33b8fc9dd73|2022-01-04 20:19:07.872005|2022-01-04 20:19:08.230000|get_stars-e40861f0-0|COMPLETED|1|2022-01-04 20:19:07.866437||2022-01-04 20:19:07.898846|2022-01-04 20:19:08.210336|1970-01-01 00:00:00.311490|e40861f01e841d03bf533259cd352bf6|0||||{"max_retries": 3, "retry_delay_seconds": 0.0}|{"repo": []}|[]|044c3280-827b-4fe9-ab91-15474a8d8526|f18fe717-179c-49eb-b9c8-f4f1378b0d43
2bf057e6-667a-470c-a678-addc47cf4de3|2022-01-04 20:19:08.243963|2022-01-04 20:19:08.553000|get_stars-e40861f0-1|COMPLETED|1|2022-01-04 20:19:08.237511||2022-01-04 20:19:08.266165|2022-01-04 20:19:08.533337|1970-01-01 00:00:00.267172|e40861f01e841d03bf533259cd352bf6|1||||{"max_retries": 3, "retry_delay_seconds": 0.0}|{"repo": []}|[]|044c3280-827b-4fe9-ab91-15474a8d8526|ffb31e39-c9dc-400b-bbf5-7ea71d39d547
sqlite> .q
```

That's it, we're out of time.

If you like to learn more:
* [Prefect Orion docs](https://orion-docs.prefect.io/)
* [Prefect Core docs](https://docs.prefect.io/)

If you'd like to go back to Prefect core with your installation:
```
pip install "prefect[viz]==0.15"
prefect version
```

## Further resources

Link collection mostly of blog posts on Prefect. Probably not really useful for you, it's rather a random link
collection, mostly things I've read or still plan to read and wanted to note down.

* https://www.prefect.io/blog/you-no-longer-need-two-separate-systems-for-batch-processing-and-streaming/
* https://www.prefect.io/blog/prefect-zero-to-hero/
* https://www.datarevenue.com/en-blog/what-we-are-loving-about-prefect
* https://medium.com/the-prefect-blog/orchestrating-elt-with-prefect-and-dbt-a-flow-of-flows-part-1-aac77126473
* https://towardsdatascience.com/orchestrate-a-data-science-project-in-python-with-prefect-e69c61a49074#67c1-8f85fb1cfe73
* https://makeitnew.io/prefect-a-modern-python-native-data-workflow-engine-7ece02ceb396
* https://rdrn.me/scaling-out-prefect/
* https://airbyte.io/recipes/elt-pipeline-prefect-airbyte-dbt
* https://airbyte.com/blog/announcing-prefect-integration-with-airbyte-to-automate-elt-pipelines
* https://www.theoaklandgroup.co.uk/prefect-should-you-utilise-the-next-generation-of-data-pipelining-software/
* https://docs.microsoft.com/en-us/events/build-may-2021/startups/breakouts/od549/
* https://youtu.be/gbzL5TIFZZY Data Science DC Aug 2021 Meetup: Machine Learning Workflow Orchestration with Prefect