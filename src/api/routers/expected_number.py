from fastapi import APIRouter, Request, Form, status
from fastapi.param_functions import Depends
from starlette.responses import RedirectResponse
from src.sessions.all_sessions import session_manager
from src.api.dependencies import get_user_or_none

router = APIRouter()


@router.post('/expected_number', response_class=RedirectResponse)
def homepage(request: Request, user: str = Depends(get_user_or_none),
             test_number: int = Form(..., ge=10, le=99)) -> RedirectResponse:
    session = session_manager.get_session(user)
    if user is None or session is None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    session.check_result(test_number)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
