from writer_assistant import WritingRequest, WriterAssistant


def test_build_prompt_contains_core_sections():
    assistant = WriterAssistant()
    request = WritingRequest(
        form="novel",
        topic="A poet loses memory in a mountain village",
        environment="Fog-heavy hill station with cedar forests and old tea houses",
        characters=["Reva", "Danish"],
    )

    prompt = assistant.build_prompt(request)

    assert "TASK" in prompt
    assert "WORLD & ENVIRONMENT" in prompt
    assert "AUTHENTICITY RULES" in prompt
    assert "A poet loses memory" in prompt
    assert "Reva, Danish" in prompt


def test_invalid_format_raises_value_error():
    assistant = WriterAssistant()
    request = WritingRequest(form="essay", topic="anything")

    try:
        assistant.build_prompt(request)
    except ValueError as exc:
        assert "Unsupported format" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported format")
