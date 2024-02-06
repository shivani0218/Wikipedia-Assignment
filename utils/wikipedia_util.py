from pydantic import BaseModel
from fastapi import HTTPException
import wikipediaapi
from collections import Counter
from logger import logger
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")
import re


class WordFrequencyParams(BaseModel):
    topic: str
    n: int


def validate_and_parse_params(params: WordFrequencyParams):
    if not params.topic:
        raise HTTPException(status_code=422, detail="Missing 'topic' parameter.")
    if params.n <= 0:
        raise HTTPException(status_code=422, detail="'n' must be a positive integer.")
    return params


def get_wikipedia_text(topic, namespace_filter=None):
    try:
        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent="Wikipedia/(singhshivani3416@gmail.com) Python/3.10",
            language="en",
        )
        page_py = wiki_wiki.page(topic)

        if page_py.exists() and "#REDIRECT" in page_py.text.upper():
            redirected_title = re.search(r"\[\[([^\]]+)\]\]", page_py.text)
            if redirected_title:
                redirected_title = redirected_title.group(1)
                page_py = wiki_wiki.page(redirected_title)

        if page_py.exists() and page_py.text:
            text = page_py.text.lower()
            if namespace_filter:
                namespace_pattern = re.compile(
                    r"\b(?:" + "|".join(namespace_filter) + r")\b", flags=re.IGNORECASE
                )
                text = " ".join(
                    match.group() for match in re.finditer(namespace_pattern, text)
                )
            return text
        else:
            return None
    except Exception as e:
        logger.error(str(e))


def analyze_text(text, n):
    try:
        stop_words = set(stopwords.words("english"))
        words = text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        word_frequencies = Counter(filtered_words)

        top_words = [
            {"word": word, "count": count}
            for word, count in word_frequencies.most_common(n)
        ]
        return top_words
    except Exception as e:
        logger.error(str(e))
