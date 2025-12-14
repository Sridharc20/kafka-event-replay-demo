
---

# 4️⃣ consumer/README.md

```md
# Consumer

This script consumes events from Kafka and builds the database state in PostgreSQL.  
It can **replay all events** from the beginning to reconstruct the `users` table.

## Usage

1. Ensure Kafka and PostgreSQL are running (`docker-compose up -d`)
2. Install dependencies:
```bash
pip install -r ../requirements.txt
