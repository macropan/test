#! /bin/sh -e

init() {
  echo "this is init step!!!"
  echo "starting to install python redis"
  pip install redis
  
  exec "$@"
}

init "$@"
