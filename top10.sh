#!/usr/bin/env bash

if [ "$#" -gt 0 ];then
    ntop=$1;
else
    ntop=10
fi

cat data/*csv | sed 's/,/ /g' | awk '{print $3, $0}' | sort -nr | head -${ntop}
    
