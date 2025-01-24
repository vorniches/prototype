#!/bin/bash

# 1) Create Django project if it doesn't exist yet
#    (If you already have the `prototype` folder with settings.py, you can skip startproject.)
if [ ! -d "prototype" ]; then
    docker run --rm -v "$(pwd)":/app -w /app python:3.10 \
      bash -c "pip install django==4.2.2 && django-admin startproject prototype ."
fi

# 2) Make sure you have an __init__.py, just in case
touch prototype/__init__.py

# 3) Create helpers folder and move openai_helper.py into it if it exists
mkdir -p prototype/helpers
if [ -f "openai_helper.py" ]; then
    mv openai_helper.py prototype/helpers/
fi

# 4) Build & run containers
docker-compose build --no-cache
docker-compose up -d

# 5) Remove the .git folder if it exists
if [ -d ".git" ]; then
    rm -rf .git
    echo ".git folder removed. You can now initialize your own Git repository."
fi
