#!/usr/bin/env bash

if [ "$#" -gt 0 ];then
    ntop=$1;
else
    ntop=10
fi

# verbose format
#cat data/*csv | sed 's/,/ /g' | awk '{print $3, $0}' | sort -nr | head -${ntop}
    
# alternative format
cat data/wiki*csv | sed 's/ /_/g' | sed 's/,/ /g' | awk '{print $3, $0}' | sort -nr | head -${ntop} | awk '{print $5, $6, $7}' | sed 's/_/ /g'
