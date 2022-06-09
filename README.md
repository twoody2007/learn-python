# learn-python

This is a start repository for a learning some basic python programming.

## installing docker on windows

Follow the instructions [here](https://docs.docker.com/desktop/windows/install/).
Below are some links for understanding how to run docker on Windows:

- [exposing ports](https://docs.docker.com/desktop/windows/networking/)
- [mounting the filesystem](https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c)

## running the program

Follow the below steps to run the program

1. spin up the docker container: `docker run ...`
2. start your python program: `uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload`
3. now click [here](http://localhost:8000)
