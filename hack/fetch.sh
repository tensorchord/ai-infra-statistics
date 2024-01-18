#!/usr/bin/env bash

set -e

# This script is used to fetch all the data.
ROOT=$(dirname "${BASH_SOURCE}")/..
cd $ROOT

for i in $(ls -d *); do
    # if the file's prefix is fetcher, then run it
    if [[ $i == fetcher* ]]; then
        echo "Fetching $i"
        python $i
    fi
done

cd - > /dev/null
