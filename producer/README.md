# Producer

This script sends user-related events to Kafka.  
It simulates an application producing events like `USER_CREATED` and `USER_UPDATED`.

## Usage

1. Ensure Kafka is running (`docker-compose up -d`)
2. Install dependencies:
```bash
pip install -r ../requirements.txt
