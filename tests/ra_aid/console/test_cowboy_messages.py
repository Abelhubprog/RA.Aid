import pytest
from ra_aid.console.cowboy_messages import get_cowboy_message, COWBOY_MESSAGES

def test_get_cowboy_message_returns_string():
    """Test that get_cowboy_message returns a non-empty string"""
    message = get_cowboy_message()
    assert isinstance(message, str)
    assert len(message) > 0

def test_cowboy_message_contains_emoji():
    """Test that returned message contains the cowboy emoji"""
    message = get_cowboy_message()
    assert '🤠' in message

def test_message_from_predefined_list():
    """Test that returned message is from our predefined list"""
    message = get_cowboy_message()
    assert message in COWBOY_MESSAGES
