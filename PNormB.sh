#!/bin/bash
cd ~/Bash-tistics 

python3 -c "import NormalDist; NormalDist.PBetween(${1}, ${2}, ${3}, ${4})"

cd ~/