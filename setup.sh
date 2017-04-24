#!/bin/bash

conda create -n mecab_env --copy -c chezou -y -q python=2 mecab

source activate mecab_env
#pip install janome
#cp -r .local/lib .conda/envs/mecab_env/
cd .conda/envs
zip -r ../../mecab_env.zip mecab_env

wget  http://www.genpaku.org/alice01/alice01j.txt -P /tmp
hdfs dfs -put /tmp/alice01j.txt /tmp/
mkdir -p resources
wget "http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg?p=*full-image" -O resources/alice-mask.jpg
