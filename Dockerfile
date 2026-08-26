FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

WORKDIR /app

COPY pyproject.toml .

RUN python -m pip install --upgrade pip \
    && python -m pip install -e .

CMD ["pytest", "tests"]