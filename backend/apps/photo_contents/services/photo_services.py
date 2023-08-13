from photo_contents.models import Photo
from photo_contents.services.patterns import (
    Context, GetChoiceWithArbitraryProbabilityDistribution)


def photo_detail(*, filters: list[str] = None) -> Photo:
    """
    Получить случайную фотографию.

    -------
    Note:
        1) Если не указаны filters, то получает случайную
           фотографию с любыми тегами
        2) Если указаны filters выбирает фотографию
           на основе указаных категорий.
        3) Использует паттерн Стратегия для возможности менять
           алгоритмы выбора фотографий.

    ---------
    :param filters: list[str] - список категорий по которой будет осуществлена
                                фильтрация фотографий.
    :return: Photo - конкретная фотография.
    """
    context = Context(GetChoiceWithArbitraryProbabilityDistribution())
    return context.get_photo(filters=filters)
