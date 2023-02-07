Для старта команда: gunicorn main:app

Для связи с конкретным ip и портом можем указать флаг -b или --bind
gunicorn main:app --bind 0.0.0.0:8000