from app.models import EventModel


def get_db_events():
    return [
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="email",
                    type="email"
                )
            ),
            timestamp="2024-12-16T10:00:00Z"
        ),
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="password",
                    type="password"
                )
            ),
            timestamp="2024-12-16T10:00:15Z"
        ),
        EventModel(
            event="$click",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="click",
                element_type="button",
                element_text="Log In",
                element_attributes=dict(
                    id="login-button",
                )
            ),
            timestamp="2024-12-16T10:00:30Z"
        ),
        EventModel(
            event="$api-call",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="",
                element_type="",
                element_text="",
                element_attributes=dict(
                    api_url="https://api.example.com/login",
                    method="POST",
                    status="200",
                )
            ),
            timestamp="2024-12-16T10:00:35Z"
        ),
        EventModel(
            event="$navigation",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="navigation",
                element_type="",
                element_text="",
                element_attributes=None
            ),
            timestamp="2024-12-16T10:00:40Z"
        ),
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="display-name",
                    type="text"
                )
            ),
            timestamp="2024-12-16T10:00:60Z"
        ),
        EventModel(
            event="$click",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="click",
                element_type="button",
                element_text="Save",
                element_attributes=dict(
                    id="save-profile",
                )
            ),
            timestamp="2024-12-16T10:00:90Z"
        ),
        EventModel(
            event="$api-call",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="",
                element_type="",
                element_text="",
                element_attributes=dict(
                    api_url="https://api.example.com/profile",
                    method="PUT",
                    status="200",
                )
            ),
            timestamp="2024-12-16T10:00:95Z"
        ),
    ]