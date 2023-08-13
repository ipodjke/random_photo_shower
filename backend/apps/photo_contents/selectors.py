from django.db.models.query import QuerySet

from photo_contents.models import Photo, Tag


def tags_list() -> QuerySet[Tag]:
    """
    Получить список всех тегов.

    :return: QuerySet[Tag] - набор тегов сервиса.
    """
    return Tag.objects.all()


def photo_list_with_amount_of_shows(*, filters: list[str] = None) -> QuerySet[Photo]:
    """
    Получить фотографии с доступным колличеством просмотров.

    --------
    Note:
        1) Функция получает фотографии тольк с количеством просмторов больше 0
        2) фильтрует только по query_params=category, остальные игнорируются

    --------
    :param filters: list[str] - список категорий по которой будет осуществлена
                                фильтрация фотографий.
    :return: QuerySet[Photo] - набор фото проекта.
    """
    filters = filters.get('category') or []
    if filters:
        return Photo.objects.filter(tags__slug__in=filters, amount_of_shows__gt=0)
    return Photo.objects.filter(amount_of_shows__gt=0)
