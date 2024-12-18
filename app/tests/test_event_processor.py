from app.processors.event_processor import EventProcessor


def test_process_events_initialization():
    processor = EventProcessor()
    assert isinstance(processor, EventProcessor)


def test_add_event_to_processor(sample_events):
    processor = EventProcessor()
    for event in sample_events:
        processor.add_event(event)

    assert len(processor.events) == len(sample_events)


def test_generate_stories(sample_events):
    processor = EventProcessor()
    for event in sample_events:
        processor.add_event(event)

    stories = processor.generate_stories()

    assert len(stories) == 2


def test_stories_names(sample_events):
    processor = EventProcessor()
    for event in sample_events:
        processor.add_event(event)

    stories = processor.generate_stories()

    assert len(stories[0].actions) == 5
    assert stories[0].name == 'login Log In'
    assert len(stories[1].actions) == 3
    assert stories[1].name == 'profile Save'
