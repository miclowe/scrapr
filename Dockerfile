FROM python:3

ADD scrapr.py /

RUN pip install bs4

CMD [ "python", "./scrapr.py"] 