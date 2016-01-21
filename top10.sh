#!/usr/bin/env bash

cat data/*csv | sed 's/,/ /g' | awk '{print $3, $0}' | sort -nr | head -10
