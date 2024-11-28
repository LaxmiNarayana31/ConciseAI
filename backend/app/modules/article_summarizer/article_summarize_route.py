from fastapi import APIRouter, Header
from app.schemas.response_schema import ResponseSchema
from app.modules.article_summarizer import article_summarize_service
from app.utils.response import msg

router = APIRouter(prefix="/api/article", tags=["Article Summarizer"])  

@router.post('/summarize', summary = "Summarize the article")
def summarize_article(article_url: str = Header(None)):
    article_response = article_summarize_service.article_summarize(article_url = article_url)
    
    if article_response == 1:
        return ResponseSchema(status = False, response = msg['provide_article_url'], data = None)
    if article_response:
        return ResponseSchema(status = True, response = msg['summarize_success'], data = article_response)
    else:
        return ResponseSchema(status = False, response = msg['summarize_failed'], data = None)