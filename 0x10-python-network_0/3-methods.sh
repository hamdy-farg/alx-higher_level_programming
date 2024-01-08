#!/usr/bin/env bash
# to give me the allowed option
curl -sI "$1" | grep  "Allow: " | cut -d" " -f 2-
