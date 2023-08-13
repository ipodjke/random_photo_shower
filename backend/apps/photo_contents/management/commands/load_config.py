import csv
import io
import shutil
from random import randint

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand

from PIL import Image

from photo_contents.models import Photo, Tag


class Command(BaseCommand):
    """
    Команда для загрузки данных при старте сервиса.

    --------
    Note:
        1) Команда используется только при старте сервиса,
           в случае выполнения на запущеном сервере приведет
           к полной очистке данных из БД
        2) Самостоятельно генерирует тестовые изображения.

    --------
    Данная команда берет файл конфигурации со строками ввида:

    http://localhost:8080/static/image1.jpg;500;flight;airlplane

    и получает из них урл картинки, количество просмтотров и теги.
    Далее создаются в БД таблица с тегами и таблица с фотографиями
    и генерируются картинки.
    """

    help = 'Создает теги а так же зогружает фото и привязывает теги к фото'
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        self._clear_data_base()
        self._delete_media_folder()
        data = self._read_data_from_config()
        self._create_tags(data)
        self._create_photos(data)

    def _clear_data_base(self) -> None:
        Tag.objects.all().delete()
        Photo.objects.all().delete()

    def _delete_media_folder(self) -> None:
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)

    def _read_data_from_config(self) -> list[list[str]]:
        with open('../data/config.csv') as csv_file:
            return [row for row in csv.reader(csv_file, delimiter=';')]

    def _create_tags(self, data: list[list[str]]) -> None:
        slugs = [slug for row in data for slug in row[2:]]
        Tag.objects.bulk_create(
            [Tag(slug=slug) for slug in set(slugs)]
        )

    def _create_photos(self, data: list[list[str]]) -> None:
        for row in data:
            url, amount_of_shows, *tags = row

            image = self._generate_image(
                name=url.split('/')[-1]
            )
            photo = Photo.objects.create(
                image=image,
                amount_of_shows=int(amount_of_shows),
            )

            tags = Tag.objects.filter(slug__in=tags)
            photo.tags.add(*tags)

    def _generate_image(self, name: str) -> SimpleUploadedFile:
        image = Image.new(
            'RGB',
            (50, 50),
            (randint(0, 255), randint(0, 255), randint(0, 255))
        )
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        return SimpleUploadedFile(
            name=name,
            content=buffer.getvalue(),
            content_type='image/jpg'
        )
