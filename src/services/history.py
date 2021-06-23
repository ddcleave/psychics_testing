from src.services.entities import Results, ResultTest, VeracityPsychicResult
from src.services.psychics import AllPsychics, VeracityPsychic


class History:
    def __init__(self, all_psychics: AllPsychics) -> None:
        self.test_history: list[ResultTest] = []
        # создаем словарь со статистикой попыток
        self.veracity_of_psychics: dict[str, VeracityPsychic] = {
            psychic.name: VeracityPsychic()
            for psychic in all_psychics.psychics
        }
        self.empty = True

    def add_test(self, result_test: ResultTest) -> None:
        self.empty = False
        self.test_history.append(result_test)
        # проверяем предсказания и обновляем словарь со статистикой
        for name, pred_number in result_test.psychic_predictions.items():
            if result_test.expected_number == pred_number:
                self.veracity_of_psychics[name].successful_attempt()
            else:
                self.veracity_of_psychics[name].unsuccessful_attempt()

    def _get_veracity(self) -> dict[str, VeracityPsychicResult]:
        return {name: veracity.get_attempts()
                for name, veracity in self.veracity_of_psychics.items()}

    def get_tests(self) -> Results:
        return Results(test_history=self.test_history,
                       veracity=self._get_veracity(),
                       empty=self.empty)
