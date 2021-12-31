#! /bin/bash -e

build() {
    echo "I am building, please wait...!!!"
    exec "$@"
}


build "$@"
