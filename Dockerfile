FROM python:3.7
RUN pip3 install python-telegram-bot --upgrade
RUN pip3 install requests
WORKDIR /usr/src
RUN mkdir bot
COPY ./bot/* /usr/src/bot/
WORKDIR /usr/src/bot
RUN mkdir persistent_data
VOLUME /usr/src/bot/persistent_data
ENV PYTHONPATH /usr/src
CMD python3 main.py
