# bunny-commit

1. Build the docker container:

```
docker build -t bunny-commit:$(git rev-parse HEAD) .  
```

2. Run the docker container

```
docker run -it bunny-commit:$(git rev-parse HEAD)
```

Thanks to [diracdeltas/tweets](https://github.com/diracdeltas/tweets) for the content.