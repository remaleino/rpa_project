FROM --platform=linux/amd64 python:3.10-slim-buster

#ARG YOUR_ENV

#ENV YOUR_ENV=${YOUR_ENV} \
#    PYTHONFAULTHANDLER=1 \
#    PYTHONUNBUFFERED=1 \
#    PYTHONHASHSEED=random \
#    PIP_NO_CACHE_DIR=off \
#    PIP_DISABLE_PIP_VERSION_CHECK=on \
#    PIP_DEFAULT_TIMEOUT=100 \
#    POETRY_VERSION=1.0.2

#RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --user --upgrade pip

RUN pip3 install -r requirements.txt
#COPY poetry.lock pyproject.toml /code/

#RUN poetry config virtualenvs.create false
#RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /code


#RUN groupadd -r xyzgroup \
#    && useradd -d /code -g xyzgroup -l -r appuser \
#    && chown -R appuser:xyzgroup /code
#USER appuser

ENTRYPOINT ["sh", "-c", "python3 src/main.py -start=$START -end=$END -s=$SUPERVISOR"]
#CMD python3 src/main.py $START $END $SUPERVISOR