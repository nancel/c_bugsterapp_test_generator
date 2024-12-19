from app.schemas.story import Story, Action


def get_stories():
    return [
        Story(
            name='login Log In',
            actions=[
                Action(
                    type="$input",
                    target="email",
                    value="",
                    url="https://example.com/login",
                    pathname="login",
                    element_text=""
                ),
                Action(
                    type="$input",
                    target="password",
                    value="",
                    url="https://example.com/login",
                    pathname="login",
                    element_text=""
                ),
                Action(
                    type="$click",
                    target="login-button",
                    value="",
                    url="https://example.com/login",
                    pathname="login",
                    element_text="Log In"
                ),
                Action(
                    type="$api-call",
                    target="",
                    value="",
                    url="https://example.com/login",
                    pathname="login",
                    element_text=""
                ),
                Action(
                    type="$navigation",
                    target="",
                    value="",
                    url="https://example.com/profile",
                    pathname="profile",
                    element_text=""
                )
            ]
        ),
        Story(
            name='profile Save',
            actions=[
                Action(
                    type="$input",
                    target="display-name",
                    value="",
                    url="https://example.com/profile",
                    pathname="profile",
                    element_text=""
                ),
                Action(
                    type="$click",
                    target="save-profile",
                    value="",
                    url="https://example.com/profile",
                    pathname="profile",
                    element_text="Save"
                ),
                Action(
                    type="$api-call",
                    target="",
                    value="",
                    url="https://example.com/profile",
                    pathname="profile",
                    element_text=""
                )
            ]
        )
    ]
