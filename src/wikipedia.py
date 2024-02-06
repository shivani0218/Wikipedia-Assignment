from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from utils.wikipedia_util import (
    validate_and_parse_params,
    get_wikipedia_text,
    analyze_text,
)
from utils.validations import WordFrequencyParams
from logger import logger

wikipedia_app = APIRouter(prefix="", tags=["wikipedia-app"])
search_history = []


async def authenticate_user(api_key: str = Header(..., convert_underscores=False)):
    if api_key != "your_secret_api_key":
        raise HTTPException(status_code=401, detail="Unauthorized")


@wikipedia_app.get("/word_frequency_analysis")
async def word_frequency_analysis(
    params: WordFrequencyParams = Depends(validate_and_parse_params),
    # authorization: bool = Depends(authenticate_user),
):
    logger.info("Starting Wikipedia word_frequency_analysis")
    try:
        topic = params.topic
        n = params.n

        article_text = get_wikipedia_text(topic)

        if article_text is None:
            raise HTTPException(status_code=404, detail="Wikipedia article not found.")

        top_words = analyze_text(article_text, n)
        result = {"topic": topic, "top_words": top_words}
        search_history.append(result)
        return JSONResponse(
            content= result,
            status_code= 200,
        )
    except HTTPException as e:
        if "validation_error" in str(e):
            return JSONResponse(status_code=422, detail="Required parameters not provided. Please provide  required parameters.")
        else:
            raise e
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))


@wikipedia_app.get("/search_history")
async def search_history_endpoint():
    if search_history:
        return search_history
    else:
        return JSONResponse(status_code=404, content = "No previous searches found.")
