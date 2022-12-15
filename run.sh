#!/bin/bash

for d in ./day*
do
    echo "==================== $d ===================="
    cd "$d"
    python "$d.py"
    cd ..
done
