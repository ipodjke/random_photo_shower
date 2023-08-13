"""
Реализация паттерна Стратегия для случайного выбора фотографии.

--------
Классы:
    1) Context - базовый класс осуществялющий контроль
       за использующейся стратегией
    2) GetChoiceWithArbitraryProbabilityDistribution - стратегия
       реализующая алгоритм основанный на встроенном в питон
       гнераторе случайных чисел с произвольным распеределением
       вероятностей

--------
Note:
    1) GetChoiceWithArbitraryProbabilityDistribution - не реализует
       механизм предотварщения появления подряд двух одинаковых элементов.
    2) Генератор из п1 в разработке.
"""

import random
from abc import ABC, abstractmethod

from django.db.models.query import QuerySet

from photo_contents.models import Photo
from photo_contents.selectors import photo_list_with_amount_of_shows


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, *, filters: list[str] = None) -> Photo:
        pass


class GetChoiceWithArbitraryProbabilityDistribution(Strategy):
    def do_algorithm(self, *, filters: list[str] = None) -> Photo:
        queryset = self._get_photos(filters=filters)

        if not queryset.exists():
            return queryset

        weight = self._get_weigth(queryset)
        photo = random.choices(queryset, weights=weight, k=1)

        photo[0].amount_of_shows -= 1
        photo[0].save()
        return photo[0]

    def _get_photos(self, *, filters: list[str] = None) -> QuerySet[Photo]:
        return photo_list_with_amount_of_shows(filters=filters)

    def _get_weigth(self, queryset: QuerySet[Photo]) -> list[int]:
        return [amount[0] for amount in queryset.values_list('amount_of_shows')]


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_photo(self, *, filters: list[str] = None) -> Photo:
        return self._strategy.do_algorithm(filters=filters)
