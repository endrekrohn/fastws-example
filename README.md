# FastWS - Example project

<p align="center">
 <a href="https://github.com/endrekrohn/fastws">
    <img src="https://raw.githubusercontent.com/endrekrohn/fastws/assets/assets/fastws.png" alt="FastWS"/>
</a>
</p>

**Source Code**: <a href="https://github.com/endrekrohn/fastws" target="_blank">https://github.com/endrekrohn/fastws</a>

---

This is an example project for how one can structure an application around FastWS. Please see read the README.md in the project repo to understand it further 👨‍💻

## Installation

You can open this project in a devcontainer using VSCode if you would like. You can use the VSCode command `Tasks: Run Task` and chooose `Run API` to start the API.

To manually install the project first install `poetry` and install the necessary dependencies with the command:

```sh
poetry install --with dev
```

Then start the API with the following command:

```sh
poetry run uvicorn api.main:app --log-level debug --host 0.0.0.0 --port 8000 --reload
```

## Questions?

If you have any questions please raise an issue or send me an email at <a href="mailto:endre@skript.no">endre@skript.no</a> 👉👉.
