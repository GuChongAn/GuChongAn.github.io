#!/bin/bash

python Tool/generateIndex.py
python Tool/generateBlog.py

git add .
git commit -m "Update"
git push



