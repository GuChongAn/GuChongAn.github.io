#!/bin/bash

python generateIndex.py
python generateBlog.py

git add .
git commit -m "Update"
git push



