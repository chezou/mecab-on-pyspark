#!/bin/bash

conda create -n mecab_env --copy -c chezou -y -q python=2 mecab

source activate mecab_env
#pip install janome
#cp -r .local/lib .conda/envs/mecab_env/
cd .conda/envs
zip -r ../../mecab_env.zip mecab_env
