from app.schemas.event import Event
from app.schemas.story import Story, Action


def split_stories_actions(events):
    stories_actions = []
    current_story_actions = []
    sequence_events = []

    for i, event in enumerate(events):
        element_attributes = event.properties.get('element_attributes')
        target = ''
        value = ''
        if element_attributes and 'id' in element_attributes:
            target = element_attributes['id']
        if element_attributes and 'value' in element_attributes:
            value = element_attributes['value']
        current_story_actions.append(
            Action(
                type=event.event,
                target=target,
                value=value,
                url=event.properties['current_url'],
                pathname=event.properties['pathname'].replace('/', ''),
                element_text=event.properties['element_text']
            )
        )
        sequence_events.append(event.event)

        sequence = ' '.join(sequence_events)
        if (
            '$click $api-call $navigation' in sequence or
            (
                '$click $api-call' in sequence and
                (
                    i + 1 >= len(events) or
                    events[i + 1].event != '$navigation')
                )
        ):
            stories_actions.append(current_story_actions)
            current_story_actions = []
            sequence_events = []

    return stories_actions


def generate_story_name(actions):
    story_name = ''
    for action in actions:
        if action.type == '$click':
            pathname = action.pathname
            element_text = action.element_text
            story_name = f'{pathname} {element_text}'
    return story_name


class EventProcessor:
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def generate_stories(self):
        stories = []

        stories_actions = split_stories_actions(self.events)

        for story_actions in stories_actions:
            story_name = generate_story_name(story_actions)
            stories.append(
                Story(name=story_name, actions=story_actions)
            )

        return stories
