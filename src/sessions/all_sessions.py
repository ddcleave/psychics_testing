from typing import Optional
from src.sessions.session import Session


class SessionManager:
    def __init__(self) -> None:
        self.all_sessions: dict[str, Session] = {}

    def create_session(self, session_id: str) -> Session:
        new_session = Session()
        self.all_sessions[session_id] = new_session
        return new_session

    def get_session(self, session_id: str) -> Optional[Session]:
        return self.all_sessions.get(session_id)

    def get_or_create_session(self, session_id: str) -> Session:
        session_id_from_db = self.get_session(session_id)
        if session_id_from_db is None:
            session_id_from_db = self.create_session(session_id)
        return session_id_from_db


session_manager = SessionManager()
