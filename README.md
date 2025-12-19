# Kafka Event Replay Demo

This repository demonstrates how Kafka can be used as an event log
to rebuild application state by replaying events.

📺 YouTube Video:
How Kafka Rebuilds Your Database (Event Replay Demo)

## Architecture

Producer → Kafka → Consumer → PostgreSQL

## Tech Stack
- Kafka
- Kafka UI
- PostgreSQL
- pgAdmin
- Python

## How to Run

1. Start infrastructure
   ```bash
   docker-compose up -d

   kafka UI: http://localhost:8080
   pgAdmin: http://localhost:5050
      email: admin@admin.com
      password: admin

2. Create Virtual Env