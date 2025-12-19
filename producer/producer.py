import json
import uuid
from datetime import datetime
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "user-events"

def send_event(event_type, data):
    event = {
        "eventId": str(uuid.uuid4()),
        "eventType": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
    producer.send(TOPIC, event)
    producer.flush()
    print(f"Sent: {event_type} → {data}")

if __name__ == "__main__":
    # Sample events
    # TIME -2 EVENTS
    send_event("USER_CREATED", {"userId": "u100", "name": "Devavratha"})
    send_event("USER_CREATED", {"userId": "u101", "name": "Dhasharatha"})
    send_event("USER_UPDATED", {"userId": "u100", "name": "Bheeshma"})
    send_event("USER_CREATED", {"userId": "u102", "name": "Rama"})
