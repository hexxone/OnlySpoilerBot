# ReinhardtBot

A telegram bot just for spoilers.
Because others won't do :>

## Build & Run with Docker

The Dockerfile will automatically set up the environment. 

Build the image with 

### Compose

First, edit your bot token in .env file

With debugging:
```bash
docker-compose up
```

For production:
```
docker-compose up -d
```


### Vanilla

```bash
docker image build -t onlyspoilerbot:0.1 .
```

With debugging:
```
docker run -it --name bot -v /home/docker/ReinhardtBot/persistent_data:/usr/src/ReinhardtBot/persistent_data -e BOT_TOKEN=<YOUR TOKEN> onlyspoilerbot:0.1
```

For production:
```
docker run --name bot -v /home/docker/ReinhardtBot/persistent_data:/usr/src/ReinhardtBot/persistent_data -e BOT_TOKEN=<YOUR TOKEN> --detach onlyspoilerbot:0.1
```


# Documentation

This bot is based on Python 3.8 and implemented according to the [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md).

## Commands

| /help         | Show Help                                 |
| ------------- | ----------------------------------------- |
| /spoiler      | Do the thing, Larry                       |