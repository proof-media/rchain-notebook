
# RChain and Python

Experimenting the interaction of Python code with the [RChain blockchain](https://www.rchain.coop/)


## how to

You can use `docker` to bring the system up. From the root of the cloned repo:

```bash
docker-compose up
```

Then open the notebook server on the address [http://localhost:8888](http://localhost:8888]); 
The password is in root folder `.env` file. 


## terminal

You can also test the library with ipython instead, with a quick container run like:

```bash
docker run --rm -it \
    --entrypoint /bin/bash python:3.7 \
    -c "pip install --upgrade rchain-grpc ipython && ipython"
```
