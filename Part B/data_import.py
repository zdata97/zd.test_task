file_path = "user/test_task/etl.json"  

df = spark.read.json(file_path)


df.write.format("delta").mode("overwrite").saveAsTable("presto.etl")
