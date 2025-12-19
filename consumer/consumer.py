import json
import psycopg2
from kafka import KafkaConsumer

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="usersdb",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
conn.autocommit = True
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    name TEXT
)
""")

group_id = "user-service-live"

# Kafka consumer replay
# group_id = "user-service-replay-v1"

TOPIC = "user-events"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    group_id=group_id,
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Consumer started...")

for message in consumer:
    event = message.value
    event_type = event["eventType"]
    data = event["data"]

    print(f"Processing {event_type}: {data}")

    if event_type == "USER_CREATED":
        cursor.execute(
            """
            INSERT INTO users (user_id, name)
            VALUES (%s, %s)
            ON CONFLICT (user_id) DO NOTHING
            """,
            (data["userId"], data["name"])
        )

    elif event_type == "USER_UPDATED":
        cursor.execute(
            """
            UPDATE users
            SET name = %s
            WHERE user_id = %s
            """,
            (data["name"], data["userId"])
        )
    
    consumer.commit()
