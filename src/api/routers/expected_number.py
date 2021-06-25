from fastapi import APIRouter, Form, Request, status
from fastapi.param_functions import Depends
from pydantic.error_wrappers import ValidationError
from src.api.dependencies import get_user_or_none
from src.models.two_digit_number import TwoDigitNumber
from src.sessions.all_sessions import session_manager
from starlette.responses import RedirectResponse

router = APIRouter()


@router.post('/expected_number', response_class=RedirectResponse)
def homepage(request: Request, user: str = Depends(get_user_or_none),
             test_number: int = Form(...)) -> RedirectResponse:
    session = session_manager.get_session(user)
    if user is None or session is None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    try:
        TwoDigitNumber(number=test_number)
    except ValidationError as e:
        session.set_errors(e.errors())
        return RedirectResponse(url="/new_test")

    session.check_result(test_number)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
