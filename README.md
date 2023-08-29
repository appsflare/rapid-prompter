# rapid-promptgen
A streamlit app to rapidly generate prompt-response pairs from the given text


# 📦 Rapid Prompt Generator 

A streamlit app to rapidly generate prompt-response pairs from the given text

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rapid-prompt-gen.streamlit.app/)


## Setup instructions

First make sure to install poetry
[Install Poetry](https://python-poetry.org/docs/#installation)

Create .env file in the project root and define ARGILLA specific env variables

```env
ARGILLA_API_KEY=
ARGILLA_API_URL=https://datasets.ai.agilityclouds.com
```


```sh
poetry install
poetry shell

```

## How to run the app

```sh
streamlit run ./configure.py
```

