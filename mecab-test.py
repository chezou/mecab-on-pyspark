# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

def word_tokenize(x):
  import MeCab as mc
  t = mc.Tagger("-Owakati -d ./MECAB/mecab_env/lib/mecab/dic/ipadic")
  return t.parse(x)


spark = SparkSession.builder \
          .appName("spark-mecab") \
          .getOrCreate()
    
data = ["こんにちは", "今日の天気は晴れです"]
dist_data = spark.sparkContext.parallelize(data)

tokenized = dist_data.map(word_tokenize).repartition(1)

!hdfs dfs -rm -r tokenizes
tokenized.saveAsTextFile('tokenizes')