# Distributed Python package with pip

![screen shot 2017-05-30 at 14 54 50](https://cloud.githubusercontent.com/assets/916653/26569856/101081ba-4548-11e7-9556-926a8d0e06f8.png)


This repo shows how to destribute packages dependented with `pip install`.

Basic idea is from [this blog](http://henning.kropponline.de/2016/09/24/running-pyspark-with-conda-env/).

## How to use

- Run `setup.sh`
- Set environment variables: `PYSPARK_PYTHON=./MECAB/mecab_env/bin/python`
- Run mecab-test.py on Workbench

## Example 2: Wordcloud

word_cloud.py shows another example with MeCab and wordcloud.

- Make sure to be able to run mecab-test.py
- Execute `!pip install wordcloud`