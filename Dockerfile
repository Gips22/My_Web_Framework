FROM python

WORKDIR /app

COPY my_web_framework /app

RUN pip install poetry
RUN poetry install

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000"]