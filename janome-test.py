# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

def word_tokenize(x):
  from janome.tokenizer import Tokenizer
  t = Tokenizer()
  tokens = t.tokenize(x.decode('utf-8'))
  return ' '.join([token.surface for token in tokens])  


spark = SparkSession.builder \
          .appName("spark-mecab") \
          .getOrCreate()
    
data = ["こんにちは", "今日の天気は晴れです"]
dist_data = spark.sparkContext.parallelize(data)

tokenized = dist_data.map(word_tokenize).repartition(1)

!hdfs dfs -rm -r tokenizes
tokenized.saveAsTextFile('tokenizes')