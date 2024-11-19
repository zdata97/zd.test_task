from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType
)

file_location = "user/test_task/csv_files/autoqa_ratings_test - autoqa_ratings.csv"
file_type = "csv"

infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

schema = StructType([
    StructField("autoqa_rating_id", StringType(), False),
    StructField("autoqa_review_id", StringType(), True),
    StructField("payment_id", IntegerType(), True),
    StructField("team_id", IntegerType(), True),
    StructField("payment_token_id", IntegerType(), True),
    StructField("external_ticket_id", IntegerType(), True),
    StructField("rating_category_id", IntegerType(), True),
    StructField("rating_category_name", StringType(), True),
    StructField("rating_scale_score", IntegerType(), True),
    StructField("score", IntegerType(), True),
    StructField("reviewee_internal_id", IntegerType(), True),
])

df = spark.read.format(file_type) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .schema(schema) \
    .load(file_location)


df.write.mode("overwrite").saveAsTable("presto.autoqa_ratings")
