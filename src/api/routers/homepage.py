from fastapi import APIRouter, Request
from fastapi.param_functions import Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import Response
from src.sessions.all_sessions import session_manager
from src.api.dependencies import get_user
from src.psychics import psychics_names

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@router.get('/', response_class=HTMLResponse)
def homepage(request: Request, user: str = Depends(get_user)) -> Response:
    session = session_manager.get_or_create_session(user)

    results = session.get_results()

    response = templates.TemplateResponse(
        "homepage.html",
        {
            "request": request,
            "history": results.test_history,
            "veracity": results.veracity,
            "psychics": psychics_names,
            "empty": results.empty
        }
    )
    response.set_cookie(key="session", value=user)
    return response
