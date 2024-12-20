from app.schemas.test import Test


class StoryProcessor:
    def __init__(self):
        self.stories = []

    def add_story(self, story):
        self.stories.append(story)

    def generate_tests(self):
        tests = []

        for story in self.stories:

            name = story.name.lower().replace(' ', '_')
            lines = [f"def test_{name}_flow(page):"]

            for i, action in enumerate(story.actions):
                if action.type == '$input':
                    id = action.target
                    value = action.value
                    lines.append(
                        f'    page.locator("#{id}").fill("{value}")'
                    )
                if action.type == '$click':
                    id = action.target
                    lines.append(
                        f'    page.locator("#{id}").click()'
                    )
                if action.type == '$navigation':
                    url = action.url
                    lines.append(
                        f'    expect(page.url()).toBe(\'{url}\')'
                    )
                if (
                    action.type == '$api-call' and
                    (
                        i + 1 >= len(story.actions) or
                        story.actions[i + 1].type != '$navigation'
                    )
                ):
                    lines.append(
                        '    success_message = '
                        'page.locator(".success-message")'
                    )
                    lines.append(
                        '    expect(success_message).to_be_visible()'
                    )

            tests.append(Test(code="\n".join(lines)))

        return tests
