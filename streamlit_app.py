# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import os

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(page_title="AI Infrastructure Statistics", page_icon=":taxi:")


# LOAD DATA ONCE
@st.cache_data
def load_data(path):
    if not os.path.isfile(path):
        path = f"https://github.com/tensorchord/ai-infra-statistics/raw/main/{path}"

    data = pd.read_csv(
        path,
        nrows=100000,  # approx. 10% of data
        names=[
            "date",
            "downloads",
            "project",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date"
        ],  # set as datetime instead of converting after the fact
    )

    return data


# STREAMLIT APP LAYOUT
st.title("AI Infrastructure Statistics")

st.markdown(
    """
This app shows the statistics of AI infrastructure projects. You could find the source code of this app here: [tensorchord/ai-infra-statistics](https://github.com/tensorchord/ai-infra-statistics).

## What is this?

This repository contains statistics about the AI Infrastructure community. We collect statistics about the most popular AI Infrastructure projects. We use these statistics to track the growth of the community. This is a work in progress. If you have any suggestions, please open an issue or a pull request.

Currently, we are collecting the following statistics:

- PyPI downloads
- DockerHub pulls

More details about the data collection can be found in the [README](https://github.com/tensorchord/ai-infra-statistics)

## Why don't you collect statistics about X?

We are happy to collect statistics about other AI Infrastructure projects. Please open an [issue or a pull request](https://github.com/tensorchord/ai-infra-statistics).

## Why don't you collect GitHub stars?

Please checkout [star-history.com](https://star-history.com/) if you are interested in GitHub stars.

We do not collect GitHub stars because we believe that GitHub stars are not a good metric for the growth of the community. Please let us know if you have any suggestions for other metrics.
"""
)

st.markdown(
    """
## VectorDB
"""
)

# DockerHub pulls

st.markdown(
    """
### DockerHub Pulls

The data is fetched from [DockerHub API](https://docs.docker.com/docker-hub/api/latest/).
"""
)

data = load_data("vectordb-raw-data-dockerhub.csv")
st.line_chart(data, x="date", y="downloads", color="project")

# PyPI downloads

st.markdown(
    """
### PyPI Downloads (4 months total)

The data is fetched from [pypistats](https://pypistats.org/).
"""
)

data = load_data("vectordb-raw-data-pypi.csv")
st.line_chart(data, x="date", y="downloads", color="project")

st.markdown(
    """
## LLM Orchestration Framework
"""
)

# PyPI downloads

st.markdown(
    """
### PyPI Downloads (4 months total)

The data is fetched from [pypistats](https://pypistats.org/).
"""
)

data = load_data("framework-llm-raw-data-pypi.csv")
st.line_chart(data, x="date", y="downloads", color="project")


st.markdown(
    """
## LLM Inference Framework
"""
)

# PyPI downloads

st.markdown(
    """
### PyPI Downloads (4 months total)

The data is fetched from [pypistats](https://pypistats.org/).
"""
)

data = load_data("framework-inference-raw-data-pypi.csv")
st.line_chart(data, x="date", y="downloads", color="project")

st.markdown(
    """
## Inference as a Service
"""
)

# PyPI downloads

st.markdown(
    """
### PyPI Downloads (4 months total)

The data is fetched from [pypistats](https://pypistats.org/).
"""
)

data = load_data("inference-raw-data-pypi.csv")
st.line_chart(data, x="date", y="downloads", color="project")

st.markdown(
    """
## Inference (Local)
"""
)

# PyPI downloads

st.markdown(
    """
### PyPI Downloads (4 months total)

The data is fetched from [pypistats](https://pypistats.org/).
"""
)

data = load_data("inference-local-raw-data-pypi.csv")
st.line_chart(data, x="date", y="downloads", color="project")
