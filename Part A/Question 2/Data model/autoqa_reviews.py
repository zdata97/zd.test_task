from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    DateType, TimestampType
)
from pyspark.sql.functions import to_date

file_location = "user/test_task/csv_files/autoqa_ratings_test - autoqa_ratings.csv"  
file_type = "csv"

infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

schema = StructType([
    StructField("autoqa_review_id", StringType(), False),    # PK
    StructField("payment_id", IntegerType(), True),          # FK
    StructField("payment_token_id", IntegerType(), True),    # FK
    StructField("external_ticket_id", IntegerType(), True),  # FK
    StructField("created_at", TimestampType(), True),
    StructField("conversation_created_at", TimestampType(), True),
    StructField("conversation_created_date", DateType(), True),
    StructField("team_id", IntegerType(), True),
    StructField("reviewee_internal_id", IntegerType(), True),
    StructField("updated_at", TimestampType(), True),
])


df = spark.read.format(file_type) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .option("dateFormat", "yyyy-MM-dd") \
    .option("timestampFormat", "yyyy-MM-dd HH:mm:ss") \
    .schema(schema) \
    .load(file_location)


df.write.mode("overwrite").saveAsTable("presto.autoqa_reviews")
