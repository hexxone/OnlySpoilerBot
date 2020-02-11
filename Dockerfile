FROM python

WORKDIR /usr/src/ReinhardtBot
COPY bot .
RUN cd bot/ && python3 -c "import bot.bot_controller"
