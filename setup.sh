#!/bin/bash

conda create -n janome_env --copy -y -q python=2

source activate janome_env
pip install janome
cp -r .local/lib .conda/envs/janome_env/
cd .conda/envs
zip -r ../../janome_env.zip janome_env
