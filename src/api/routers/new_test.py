from fastapi import APIRouter, Request, status
from fastapi.param_functions import Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, Response
from src.sessions.all_sessions import session_manager
from src.api.dependencies import get_user_or_none
from src.psychics import psychics_names


router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@router.post('/new_test', response_class=Response)
def homepage(request: Request,
             user: str = Depends(get_user_or_none)) -> Response:
    session = session_manager.get_session(user)
    if user is None or session is None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    predictions = session.create_predictions()

    return templates.TemplateResponse(
        "new_test.html",
        {
            "request": request,
            "predictions": predictions,
            "psychics": psychics_names
        }
    )
