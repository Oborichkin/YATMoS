FROM python:3

WORKDIR /usr/src/app

COPY setup.py ./
COPY yatmos ./yatmos

RUN pip install -e .

CMD ["python", "-m", "uvicorn", "yatmos.main:app", "--host", "0.0.0.0"]
