from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    DateType, TimestampType, FloatType, BooleanType
)

file_location = "user/test_task/csv_files/manual_reviews_test - manual_reviews.csv"
file_type = "csv"

infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

schema = StructType([
    StructField("review_id", IntegerType(), False),
    StructField("payment_id", IntegerType(), True),
    StructField("payment_token_id", IntegerType(), True),
    StructField("created", TimestampType(), True),
    StructField("conversation_created_at", TimestampType(), True),
    StructField("conversation_created_date", DateType(), True),
    StructField("conversation_external_id", IntegerType(), True),
    StructField("team_id", IntegerType(), True),
    StructField("reviewer_id", IntegerType(), True),
    StructField("reviewee_id", IntegerType(), True),
    StructField("comment_id", IntegerType(), True),
    StructField("scorecard_id", IntegerType(), True),
    StructField("scorecard_tag", StringType(), True),
    StructField("score", FloatType(), True),
    StructField("updated_at", TimestampType(), True),
    StructField("updated_by", IntegerType(), True),
    StructField("assignment_review", BooleanType(), True),
    StructField("seen", BooleanType(), True),
    StructField("disputed", BooleanType(), True),
    StructField("review_time_seconds", StringType(), True),
    StructField("assignment_name", StringType(), True),
    StructField("imported_at", TimestampType(), True)
])

df = spark.read.format(file_type) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .schema(schema) \
    .load(file_location)


df.write.mode("overwrite").saveAsTable("presto.manual_reviews")
