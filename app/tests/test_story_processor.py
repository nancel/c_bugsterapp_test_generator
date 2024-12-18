from app.processors.story_processor import StoryProcessor


def test_process_stories_initialization(sample_story):
    processor = StoryProcessor(sample_story)
    assert isinstance(processor, StoryProcessor)
    assert processor.story.name == 'login Log In'


def test_generate_test(sample_story):
    processor = StoryProcessor(sample_story)

    test = processor.generate_test()

    expected = """def test_login_log_in_flow(page):
    page.locator("#email").fill("email_value")
    page.locator("#password").fill("password_value")
    page.locator("#login-button").click()
    expect(page.url()).toBe('https://example.com/profile')"""

    assert test.strip() == expected.strip()
