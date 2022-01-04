#! /bin/sh -e

init() {
  echo "this is init step!!!"

  exec "$@"
}

init "$@"
