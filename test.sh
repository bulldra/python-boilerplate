#!/bin/bash

if [ $# == 1 ]; then
    TEST_PATH="$1"
else
    TEST_PATH=""
fi
docker-compose run --entrypoint "pytest -s $TEST_PATH" python-boilerplate
docker-compose down
