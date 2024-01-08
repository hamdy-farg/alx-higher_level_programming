#!/usr/bin/env bash
curl -s "$1" | grep -l "Allow:"| awk '{print }'
