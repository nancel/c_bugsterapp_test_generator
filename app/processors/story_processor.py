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

            for action in story.actions:
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

            tests.append("\n".join(lines))

        return tests
