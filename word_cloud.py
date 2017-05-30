## NLP example: Wordcloud of "alice in wonder land"
# Basic code is taken from https://github.com/amueller/word_cloud/blob/master/examples/masked.py

from pyspark.sql import SparkSession
from wordcloud import WordCloud, STOPWORDS

def word_tokenize(x):
  import MeCab as mc
  t = mc.Tagger("-Owakati  -d ./MECAB/mecab_env/lib/mecab/dic/ipadic -r ./MECAB/mecab_env/etc/mecabrc")
  
  return t.parse(x.encode('utf-8'))


spark = SparkSession.builder \
      .appName("Word count") \
      .getOrCreate()
    
threshold = 5

# Download from http://www.genpaku.org/alice01/alice01j.txt
# Written by: Lewis Carroll
# Translated by: Hiroo Yamagata

text_file = spark.sparkContext.textFile("/tmp/alice01j_utf8.txt")

stopwords = set(STOPWORDS)

counts = text_file.map(lambda line: word_tokenize(line)) \
             .flatMap(lambda line: line.split(" ")) \
             .filter(lambda word: len(word.decode('utf-8')) >= 3) \
             .map(lambda word: (word.decode('utf-8'), 1)) \
             .reduceByKey(lambda a, b: a + b)

from pyspark.sql.types import *
schema = StructType([StructField("word", StringType(), True),
                     StructField("frequency", IntegerType(), True)])

filtered = counts.filter(lambda pair: pair[1] >= threshold)
counts_df = spark.createDataFrame(filtered, schema)

frequencies = counts_df.toPandas().set_index('word').T.to_dict('records')

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

alice_mask = np.array(Image.open(path.join("resources", "alice-mask.jpg")))

FONT_PATH = path.expanduser("~/.font/NotoSansCJKjp-Regular.otf")
wc = WordCloud(font_path=FONT_PATH,
               background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
wc.generate_from_frequencies(dict(*frequencies))

plt.imshow(wc, interpolation='bilinear')
