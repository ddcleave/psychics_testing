from random import randint, sample

from src.services.entities import VeracityPsychicResult


class Psychic:
    def __init__(self, name: str) -> None:
        self.name = name

    def prediction(self) -> int:
        return randint(10, 99)


class VeracityPsychic:
    def __init__(self) -> None:
        self.successful_attempts: int = 0
        self.attempts: int = 0

    def successful_attempt(self) -> None:
        self.successful_attempts += 1
        self.attempts += 1

    def unsuccessful_attempt(self) -> None:
        self.attempts += 1

    def get_attempts(self) -> VeracityPsychicResult:
        return VeracityPsychicResult(
            successful_attempts=self.successful_attempts,
            attempts=self.attempts
        )


class AllPsychics:
    def __init__(self, list_psychic: list[str]) -> None:
        if len(list_psychic) < 2:
            raise ValueError
        self.psychics = [Psychic(name) for name in list_psychic]

    def get_predictions(self) -> dict[str, int]:
        test_group = sample(self.psychics, randint(2, len(self.psychics)))
        return {psychic.name: psychic.prediction()
                for psychic in test_group}
