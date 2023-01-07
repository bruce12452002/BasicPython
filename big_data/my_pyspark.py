# 須先下載 pyspark 才可以 import
# 輸入 -> 計算 -> 輸出
# 從 SparkContext 為入口
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
context = SparkContext(conf=conf)
print(context.version)

rdd_list = context.parallelize([1, 2, 3])
rdd_tuple = context.parallelize((1, 2, 3))
rdd_set = context.parallelize({1, 2, 3})
rdd_dict = context.parallelize({"k1": 1, "k2": 2, "k3": 3})
rdd_str = context.parallelize("123一二三")

print(rdd_list.collect())
print(rdd_tuple.collect())
print(rdd_set.collect())
print(rdd_dict.collect())  # dict 只會保留 key
print(rdd_str.collect())  # str 會一個字一個字分開
rdd = context.textFile("../test.txt")
print(f"{rdd.collect()}, {type(rdd.collect())}")  # 取得的是 list，每一行算一個 index
context.stop()
