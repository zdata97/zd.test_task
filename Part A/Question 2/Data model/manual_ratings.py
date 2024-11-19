from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    FloatType, BooleanType
)

file_location = "user/test_task/csv_files/manual_rating_test - manual_rating.csv"
file_type = "csv"

infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

schema = StructType([
    StructField("review_id", IntegerType(), False),
    StructField("category_id", IntegerType(), False),
    StructField("payment_id", IntegerType(), True),
    StructField("team_id", IntegerType(), True),
    StructField("rating", IntegerType(), True),
    StructField("cause", StringType(), True),
    StructField("rating_max", IntegerType(), True),
    StructField("weight", FloatType(), True),
    StructField("critical", BooleanType(), True),
    StructField("category_name", StringType(), True)
])

df = spark.read.format(file_type) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .schema(schema) \
    .load(file_location)



df.write.mode("overwrite").saveAsTable("presto.manual_ratings")
