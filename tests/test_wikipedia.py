import pytest
import json
from fastapi.testclient import TestClient
from app import app
from tests.test_data_wikipedia import (
    valid_input,
    missing_topic,
    negative_n,
    missing_n,
    invalid_namespace_filter,
    test_data_list,
)


class TestWordFrequencyAnalysis:

    @pytest.fixture
    def client(self):
        return TestClient(app)

    @pytest.mark.parametrize("test_data", test_data_list)
    def test_word_frequency_analysis(self, client, test_data):
        response = client.get("/word_frequency_analysis", params=test_data)

        assert response.status_code == 200

        result = response.json()
        assert "topic" in result
        assert "top_words" in result

        if "topic" in test_data:
            assert result["topic"] == test_data["topic"]

        if "n" in test_data:
            if test_data["n"] > 0:
                assert len(result["top_words"]) <= test_data["n"]

        if "namespace_filter" in test_data:
            if isinstance(test_data["namespace_filter"], list):
                assert all(
                    any(
                        namespace.lower() in word.lower()
                        for namespace in test_data["namespace_filter"]
                    )
                    for word in result["top_words"]
                )

    def test_word_frequency_analysis_missing_topic(self, client):
        response = client.get("/word_frequency_analysis", params=missing_topic)

        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "Field required"

    def test_word_frequency_analysis_negative_n(self, client):
        response = client.get("/word_frequency_analysis", params=negative_n)

        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "'n' must be a positive integer."

    def test_word_frequency_analysis_missing_n(self, client):
        print(missing_n)
        response = client.get("/word_frequency_analysis", params=json.dumps(missing_n))
        print(response.text)

        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "'n' must be a positive integer."
