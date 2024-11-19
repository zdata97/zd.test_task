from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    DateType, TimestampType, FloatType, BooleanType
)

file_location = "user/test_task/csv_files/conversations_test - conversations.csv"
file_type = "csv"

infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

schema = StructType([
    StructField("external_ticket_id", IntegerType(), False),
    StructField("payment_id", IntegerType(), False),
    StructField("payment_token_id", IntegerType(), False),
    StructField("conversation_created_at", TimestampType(), True),
    StructField("conversation_created_at_date", DateType(), True),
    StructField("channel", StringType(), True),
    StructField("assignee_id", IntegerType(), True),
    StructField("updated_at", TimestampType(), True),
    StructField("closed_at", TimestampType(), True),
    StructField("message_count", IntegerType(), True),
    StructField("last_reply_at", TimestampType(), True),
    StructField("language", StringType(), True),
    StructField("imported_at", TimestampType(), True),
    StructField("unique_public_agent_count", IntegerType(), True),
    StructField("public_mean_character_count", FloatType(), True),
    StructField("public_mean_word_count", FloatType(), True),
    StructField("private_message_count", IntegerType(), True),
    StructField("public_message_count", IntegerType(), True),
    StructField("klaus_sentiment", StringType(), True),
    StructField("is_closed", BooleanType(), True),
    StructField("agent_most_public_messages", IntegerType(), True),
    StructField("first_response_time", IntegerType(), True),
    StructField("first_resolution_time_seconds", IntegerType(), True),
    StructField("full_resolution_time_seconds", IntegerType(), True),
    StructField("most_active_internal_user_id", IntegerType(), True),
    StructField("deleted_at", TimestampType(), True)
])

df = spark.read.format(file_type) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .schema(schema) \
    .load(file_location)


df.write.mode("overwrite").saveAsTable("presto.conversations")
