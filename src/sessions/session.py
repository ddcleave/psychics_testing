from src.services.entities import ResultTest, Results
from src.services.history import History
from src.psychics import all_psychics


class Session:
    def __init__(self) -> None:
        self.history = History(all_psychics)
        self.predictions: dict[str, int] = {}
        self.errors: list[dict] = []

    def _create_predictions(self) -> dict[str, int]:
        self.predictions = all_psychics.get_predictions()
        return self.predictions

    def get_or_create_predictions(self) -> dict[str, int]:
        if self.errors == []:
            return self._create_predictions()
        return self.predictions

    def check_result(self, expected_number: int) -> None:
        self.errors = []
        self.history.add_test(
            ResultTest(expected_number=expected_number,
                       psychic_predictions=self.predictions)
        )

    def get_results(self) -> Results:
        return self.history.get_tests()

    def set_errors(self, errors: list[dict]) -> None:
        self.errors = errors
