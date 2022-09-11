FROM python:3.7

WORKDIR /kpt_intelli_design

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn -w 1 -b 0.0.0.0:5002 main:app