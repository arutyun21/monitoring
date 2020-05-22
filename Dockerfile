FROM python:3.6

RUN pip3 install graphyte requests
RUN mkdir /code
COPY run.py /code/run.py
WORKDIR /code
ENTRYPOINT ["python", "run.py"]