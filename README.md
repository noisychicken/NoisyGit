# NoisyGit
Listens to stuff happening on GitHub and loudly speaks them out

##


Boot the redis:

```
docker-compose up -d
```

Install the deps:
```
pipenv install
```

Start the worker process

```
pipenv run rq worker
```

Start the web API:

```
FLASK_ENV=development pipenv run python main.py
```

## Queue status
[http://localhost:8080/rq/](http://localhost:8080/rq/)
