# Procesador de eventos web para generación de casos y tests

### **1. Recibe eventos de interacción de usuario**

```json
[
    {
        "event": "$input",
        "properties": {
            "distinct_id": "user_12345",
            "session_id": "session_67890",
            "journey_id": "journey_001",
            "current_url": "https://example.com/login",
            "host": "example.com",
            "pathname": "/login",
            "browser": "Chrome",
            "device": "Desktop",
            "event_type": "input",
            "element_type": "input",
            "element_text": "",
            "element_attributes": {
                "id": "email",
                "type": "email",
                "value": "user@example.com"
            }
        },
        "timestamp": "2024-12-16T10:00:00Z"
    },
    {
        "event": "$input",
        "properties": {
            "distinct_id": "user_12345",
            "session_id": "session_67890",
            "journey_id": "journey_001",
            "current_url": "https://example.com/login",
            "host": "example.com",
            "pathname": "/login",
            "browser": "Chrome",
            "device": "Desktop",
            "event_type": "input",
            "element_type": "input",
            "element_text": "",
            "element_attributes": {
                "id": "password",
                "type": "password",
                "value": "**********"
            }
        },
        "timestamp": "2024-12-16T10:00:10Z"
    },
    {
        "event": "$click",
        "properties": {
            "distinct_id": "user_12345",
            "session_id": "session_67890",
            "journey_id": "journey_001",
            "current_url": "https://example.com/login",
            "host": "example.com",
            "pathname": "/login",
            "browser": "Chrome",
            "device": "Desktop",
            "event_type": "click",
            "element_type": "button",
            "element_text": "Log In",
            "element_attributes": {
                "id": "login-button"
            }
        },
        "timestamp": "2024-12-16T10:00:15Z"
    },
    ....
]

```

### **2. Los agrupa en "historias de usuario" basadas en patrones de comportamiento**

```json
[
  {
    "name": "login Log In",
    "actions": [
      {
        "type": "$input",
        "target": "email",
        "value": "user@example.com",
        "url": "https://example.com/login",
        "pathname": "login",
        "element_text": ""
      },
      {
        "type": "$input",
        "target": "password",
        "value": "**********",
        "url": "https://example.com/login",
        "pathname": "login",
        "element_text": ""
      },
      {
        "type": "$click",
        "target": "login-button",
        "value": "",
        "url": "https://example.com/login",
        "pathname": "login",
        "element_text": "Log In"
      },
      {
        "type": "$api-call",
        "target": "",
        "value": "",
        "url": "https://example.com/login",
        "pathname": "login",
        "element_text": ""
      },
      {
        "type": "$navigation",
        "target": "",
        "value": "",
        "url": "https://example.com/profile",
        "pathname": "profile",
        "element_text": ""
      }
    ]
  }
]
```

### **3. Genera tests E2E en Playwright basados en estas historias**

```json
[
  {
    "code": "def test_login_log_in_flow(page):\n    page.locator(\"#email\").fill(\"user@example.com\")\n    page.locator(\"#password\").fill(\"**********\")\n    page.locator(\"#login-button\").click()\n    expect(page.url()).toBe('https://example.com/profile')"
  }
]
```

## **Installation and Execution Instructions**

### **Prerequisites**

- Docker and Docker Compose installed.

### **Build and Run with Docker**

```bash
docker compose build
docker compose up --build
```

### **Run Tests**

```bash
docker compose run api pytest
```

## **API Documentation**

### **Swagger**

```bash
http://0.0.0.0:8000/docs
```

## **Improvement**

- **Scalability**: Implement processing queues (e.g., RabbitMQ, Celery) to handle large volumes of events. Implemented in the branch https://github.com/nancel/c_bugsterapp_test_generator/tree/celery-rabbit. (Tests and configuration improvements are still pending)
- **User story identification algorithm**: Use a rule engine or machine learning.
