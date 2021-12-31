#! /bin/bash -e

deploy () {
    cd docker
    /usr/bin/docker build -t test-redis-py:v1.0.0 .
    exec "$@"
}

deploy "$@"
