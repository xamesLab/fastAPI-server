#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
    echo "Starting celery..."
    celery --app=tasks:tasks:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
    echo "Starting flower..."
    celery --app=tasks:tasks:celery flower
fi