from app.schemas.event import Event
from app.schemas.story import Story, Action


def extract_action(event):
    element_attributes = event.element_attributes

    return Action(
        type=event.event,
        target=element_attributes.get('id', ''),
        value=element_attributes.get('value', ''),
        url=event.current_url,
        pathname=event.pathname.replace('/', ''),
        element_text=event.element_text
    )


def should_split_story(sequence, events, index):
    return (
        '$click $api-call $navigation' in sequence or
        (
            '$click $api-call' in sequence and
            (
                index + 1 >= len(events) or
                events[index + 1].event != '$navigation')
            )
    )


def split_stories_actions(events):
    stories_actions = []
    current_story_actions = []
    sequence_events = []

    for i, event in enumerate(events):
        current_story_actions.append(
            extract_action(event)
        )
        sequence_events.append(event.event)

        sequence = ' '.join(sequence_events)
        if should_split_story(sequence, events, i):
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
