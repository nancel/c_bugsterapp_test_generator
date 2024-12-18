class StoryProcessor:
    def __init__(self, story):
        self.story = story

    def generate_test(self):
        name = self.story.name.lower().replace(' ', '_')
        lines = [f"def test_{name}_flow(page):"]

        for action in self.story.actions:
            if action.type == '$input':
                id = action.target
                lines.append(
                    f'    page.locator("#{id}").fill("{id}_value")'
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

        return "\n".join(lines)
