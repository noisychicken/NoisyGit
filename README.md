# NoisyGit
Listens to stuff happening on GitHub and loudly speaks them out

##


Boot the redis:

```
docker-compose up -d
```

Start the worker process

```
pipenv run rq worker
```

Start the web API:

```
FLASK_ENV=development pipenv run python main.py
```
