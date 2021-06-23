from typing import Optional
from uuid import uuid4

from fastapi import Cookie


def get_user(session: Optional[str] = Cookie(None)) -> str:
    if session is None:
        return str(uuid4())
    else:
        return session


def get_user_or_none(session: Optional[str] = Cookie(None)) -> Optional[str]:
    if session is None:
        return None
    else:
        return session
