FROM python:3.10-buster

ENV DEBIAN_FRONTEND noninteractive
COPY pyproject.toml poetry.loc[k] /
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -  && \
    echo "export PATH=\"$HOME/.poetry/bin:$PATH\"" > ~/.bashrc && \
    export PATH="$HOME/.poetry/bin:$PATH"  && \
    poetry config virtualenvs.create false && \
    poetry install