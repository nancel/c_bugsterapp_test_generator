

def test_create_event(client, sample_tests):
    response = client.post("/api/events", json=sample_tests)

    assert response.status_code == 200


def test_get_events(client):
    response = client.get("/api/events")

    assert response.status_code == 200
    events = response.json()
    assert len(events) == 8
    assert events[0] == {
        "event": "$input",
        "timestamp": "2024-12-16T10:00:00Z",
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
        },
        "id": 1
    }


def test_get_stories(client):
    response = client.get("/api/stories")

    assert response.status_code == 200
    stories = response.json()['stories']
    assert len(stories) == 2
    assert stories[0] == {
        "name": "login Log In",
        "actions": [
            {
                "type": "$input",
                "target": "email",
                "value": "",
                "url": "https://example.com/login",
                "pathname": "login",
                "element_text": ""
            },
            {
                "type": "$input",
                "target": "password",
                "value": "",
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


def test_get_tests(client):
    response = client.get("/api/tests")

    assert response.status_code == 200
    tests = response.json()['tests']
    assert len(tests) == 2
    assert tests[0] == """def test_login_log_in_flow(page):
    page.locator("#email").fill("email_value")
    page.locator("#password").fill("password_value")
    page.locator("#login-button").click()
    expect(page.url()).toBe('https://example.com/profile')"""
