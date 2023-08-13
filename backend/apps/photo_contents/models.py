from django.core.validators import MinValueValidator
from django.db import models


class Tag(models.Model):
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'<Tag[slug={ self.slug }]>'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Photo(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='./',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги фотографии',
        related_name='photos'
    )
    amount_of_shows = models.PositiveIntegerField(
        verbose_name='Колличество показов картинки',
        validators=[
            MinValueValidator(
                1,
                'Создавать фотографии без просмотров запрещено!'
            ),
        ]
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('-amount_of_shows',)

    def __str__(self):
        return f'<Photo[id = { self.id } | Оставшитеся показы { self.amount_of_shows }]>'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
