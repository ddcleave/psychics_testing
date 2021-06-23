from pydantic import BaseModel


class PredictionPsychic(BaseModel):
    name: str
    prediction: int


class ResultTest(BaseModel):
    expected_number: int
    psychic_predictions: dict[str, int]


class VeracityPsychicResult(BaseModel):
    successful_attempts: int
    attempts: int


class Results(BaseModel):
    test_history: list[ResultTest]
    veracity: dict[str, VeracityPsychicResult]
    empty: bool
