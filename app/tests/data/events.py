def get_events():
    return [
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
        {
            "event": "$api-call",
            "properties": {
                "distinct_id": "user_12345",
                "session_id": "session_67890",
                "journey_id": "journey_001",
                "current_url": "https://example.com/login",
                "host": "api.example.com",
                "pathname": "/login",
                "browser": "Chrome",
                "device": "Desktop",
                "event_type": "",
                "element_type": "",
                "element_text": "",
                "element_attributes": {
                    "api_url": "https://api.example.com/login",
                    "method": "POST",
                    "status": "200"
                }
            },
            "timestamp": "2024-12-16T10:00:17Z"
        },
        {
            "event": "$navigation",
            "properties": {
                "distinct_id": "user_12345",
                "session_id": "session_67890",
                "journey_id": "journey_001",
                "current_url": "https://example.com/profile",
                "host": "example.com",
                "pathname": "/profile",
                "browser": "Chrome",
                "device": "Desktop",
                "event_type": "navigation",
                "element_type": "",
                "element_text": "",
                "element_attributes": {}
            },
            "timestamp": "2024-12-16T10:00:20Z"
        },
        {
            "event": "$input",
            "properties": {
                "distinct_id": "user_12345",
                "session_id": "session_67890",
                "journey_id": "journey_001",
                "current_url": "https://example.com/profile",
                "host": "example.com",
                "pathname": "/profile",
                "browser": "Chrome",
                "device": "Desktop",
                "event_type": "input",
                "element_type": "input",
                "element_text": "",
                "element_attributes": {
                    "id": "display-name",
                    "type": "text",
                    "value": "John Doe"
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
                "current_url": "https://example.com/profile",
                "host": "example.com",
                "pathname": "/profile",
                "browser": "Chrome",
                "device": "Desktop",
                "event_type": "click",
                "element_type": "button",
                "element_text": "Save",
                "element_attributes": {
                    "id": "save-profile"
                }
            },
            "timestamp": "2024-12-16T10:00:15Z"
        },
        {
            "event": "$api-call",
            "properties": {
                "distinct_id": "user_12345",
                "session_id": "session_67890",
                "journey_id": "journey_001",
                "current_url": "https://example.com/profile",
                "host": "api.example.com",
                "pathname": "/profile",
                "browser": "Chrome",
                "device": "Desktop",
                "event_type": "",
                "element_type": "",
                "element_text": "",
                "element_attributes": {
                    "api_url": "https://api.example.com/profile",
                    "method": "PUT",
                    "status": "200"
                }
            },
            "timestamp": "2024-12-16T10:00:17Z"
        }
    ]
