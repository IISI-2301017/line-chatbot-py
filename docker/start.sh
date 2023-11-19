#!/bin/bash

cd ..
docker run --restart=always -dp 8080:8080 -v "$(pwd):/damn"  --name linebot python_flask:latest
