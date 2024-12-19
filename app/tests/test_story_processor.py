from app.processors.story_processor import StoryProcessor


def test_process_stories_initialization():
    processor = StoryProcessor()
    assert isinstance(processor, StoryProcessor)


def test_add_story(sample_stories):
    processor = StoryProcessor()
    for story in sample_stories:
        processor.add_story(story)

    assert len(processor.stories) == len(sample_stories)


def test_generate_test(sample_stories):
    processor = StoryProcessor()
    for story in sample_stories:
        processor.add_story(story)

    tests = processor.generate_tests()

    expected_0 = """def test_login_log_in_flow(page):
    page.locator("#email").fill("email_value")
    page.locator("#password").fill("password_value")
    page.locator("#login-button").click()
    expect(page.url()).toBe('https://example.com/profile')"""
    assert tests[0].strip() == expected_0.strip()

    expected_1 = """def test_profile_save_flow(page):
    page.locator("#display-name").fill("display-name_value")
    page.locator("#save-profile").click()"""
    assert tests[1].strip() == expected_1.strip()
