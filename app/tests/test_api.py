

def test_create_event(client):
    response = client.post("/api/events", json=[
        {
            "event": "$input",
            "timestamp": "2024-12-16T10:00:00Z",
            "id": 1,
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
                    "type": "email"
                }
            }
        },
        {
            "event": "$input",
            "timestamp": "2024-12-16T10:00:10Z",
            "id": 2,
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
                    "type": "password"
                }
            }
        }
    ])
    assert response.status_code == 200


def test_get_events(client):
    response = client.get("/api/events")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_stories(client):
    response = client.get("/api/stories")
    assert response.status_code == 200
