# OnlySpoilerBot

### Credits to: ReinhardtBot

A telegram bot just for spoilers.
Because others won't do :>

## Build & Run with Docker

The Dockerfile will automatically set up the environment. 

Compose file is also included.

### Compose

First, edit `BOTTOKEN` in `.env` file.
Then continue below:

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
docker run -it --name bot -e BOT_TOKEN=<YOUR TOKEN> onlyspoilerbot:0.1
```

For production:
```
docker run --name bot -e BOT_TOKEN=<YOUR TOKEN> --detach onlyspoilerbot:0.1
```


# Documentation

This bot is based on Python 3.8 and implemented according to the [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md).

## Commands

NONE.

just use Inline ```@OnlySpoilerBot <hide me>```