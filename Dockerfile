FROM python:3.10.8

RUN pip install requests
COPY bunny-animate.py .

ENTRYPOINT ["python3", "bunny-animate.py"]