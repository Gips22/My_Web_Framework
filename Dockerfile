FROM python

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry install

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000"]