# 🚀 Notification Service

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/)
[![SQLite](https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A robust, queue-based notification service built with **FastAPI**, **RabbitMQ**, and **SQLite**. This service efficiently handles **Email**, **SMS**, and **In-app** notifications with built-in retry logic and asynchronous processing.

## ✨ Features

✅ **REST API with FastAPI**
   - Fast and modern API framework
   - Automatic OpenAPI documentation
   - Type checking and validation

✅ **Queue-based Processing**
   - RabbitMQ message broker
   - Asynchronous message handling
   - Guaranteed message delivery

✅ **Multiple Notification Channels**
   - Email notifications
   - SMS notifications
   - In-app notifications

✅ **Robust Error Handling**
   - Automatic retry mechanism
   - Failed notification tracking
   - Detailed error logging

✅ **Data Persistence**
   - SQLite database
   - SQLAlchemy ORM
   - Easy to scale

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- RabbitMQ Server
- SQLite3

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/AdityaTyagi44/notification-service.git
   cd notification-service
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up RabbitMQ
   ```bash
   # Start RabbitMQ Server
   # Windows: RabbitMQ will start automatically after installation
   # Using Docker (recommended)
   docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```

4. Initialize the database
   ```bash
   python -m app.init_db
   #This will create a test user with the following ID:
   #user_id: 1111-2222-3333-4444
   ```
   

5. Start the services
   ```bash
   # Terminal 1: Start the API server
   uvicorn app.main:app --reload

   # Terminal 2: Start the worker
   python run_worker.py
   ```

## 📡 API Usage

### Send a Notification

```bash
# Send an email notification
POST /notifications

{
    "user_id": "1111-2222-3333-4444",
    "type": "email",
    "content": "Welcome to the platform!"
    }
}
```

### Get User Notifications

```bash
# Get all notifications for a user
GET /users/{user_id}/notifications

Response:
{
  "id": "1111-2222-3333-4444",
  "name": "Aditya Tyagi",
  "email": "aditya@example.com",
  "phone": "9876543210",
  "notifications": [
    {
      "type": "email",
      "content": "Hello Aditya!",
      "status": "sent",
      "sent_at": "2025-05-17T18:45:00"
    }
  ]
}
```

## 🏗️ Project Structure

```plaintext
notification_service/
├── app/
│   ├── utils/
│   │   ├── email_sender.py    # Email notification handler
│   │   ├── sms_sender.py      # SMS notification handler
│   │   └── inapp_sender.py    # In-app notification handler
│   ├── database.py            # Database configuration
│   ├── init_db.py            # Database initialization
│   ├── main.py               # FastAPI application
│   ├── models.py             # SQLAlchemy models
│   ├── routes.py             # API endpoints
│   ├── schemas.py            # Pydantic schemas
│   └── worker.py             # Background worker
├── notifications.db          # SQLite database
├── read_users.py            # User management utility
├── requirements.txt         # Project dependencies
└── run_worker.py           # Worker process starter
```

## 🔧 Configuration

The service can be configured through environment variables:

- `RABBITMQ_URL`: RabbitMQ connection URL (default: `amqp://guest:guest@localhost/`)
- `DATABASE_URL`: SQLite database URL (default: `sqlite:///notifications.db`)
- `RETRY_COUNT`: Maximum retry attempts for failed notifications (default: `3`)

## 📄 Assumptions

- The user database is pre-populated manually (via `init_db.py`) for testing purposes.
- Notifications are not actually sent over the internet:
  - **Email** and **SMS** are mocked (they are printed to the console).
  - **In-app** notifications are stored in the database and returned via API.
- There is no authentication or user login system.
- Only one queue (`notifications`) is used for simplicity.
- SQLite is used as the database for easy local development and portability.
- Environment variables like `RABBITMQ_URL` or `RETRY_COUNT` are not required to be set unless customization is needed.


---

⭐ Star this repository if you find it helpful!


 
