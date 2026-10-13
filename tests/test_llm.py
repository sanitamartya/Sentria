
from unittest.mock import Mock, patch

import pytest
from pydantic import SecretStr

from sentria import llm


def test_ask_model_returns_generated_text():
    fake_response = Mock()
    fake_response.text = "Sentria test successful"

    with patch.object(llm.genai, "Client") as client_class:
        client = client_class.return_value
        client.models.generate_content.return_value = fake_response

        with patch.object(
            llm.settings,
            "gemini_api_key",
            SecretStr("test-key"),
        ):
            result = llm.ask_model("Say hello")

    assert result == "Sentria test successful"
    client.models.generate_content.assert_called_once_with(
        model="gemini-3.8-flash",
        contents="Say hello",
    )


def test_ask_model_requires_api_key():
    with patch.object(llm.settings, "gemini_api_key", None):
        with pytest.raises(
            RuntimeError,
            match="GEMINI_API_KEY is not configured",
        ):
            llm.ask_model("Say hello")


def test_ask_model_rejects_empty_response():
    fake_response = Mock()
    fake_response.text = None

    with patch.object(llm.genai, "Client") as client_class:
        client = client_class.return_value
        client.models.generate_content.return_value = fake_response

        with patch.object(
            llm.settings,
            "gemini_api_key",
            SecretStr("test-key"),
        ):
            with pytest.raises(
                RuntimeError,
                match="Gemini returned no text response",
            ):
                llm.ask_model("Say hello")
