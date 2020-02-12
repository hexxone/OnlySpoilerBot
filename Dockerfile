FROM python:3.7

WORKDIR /usr/src/ReinhardtBot/bot
COPY bot .
RUN pip3 install python-telegram-bot --upgrade
RUN pip3 install requests
ENV PYTHONPATH /usr/src/ReinhardtBot
CMD python3 bot_controller.py