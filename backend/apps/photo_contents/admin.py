from django.contrib import admin

from photo_contents.models import Photo, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_of_shows')
    filter_horizontal = ('tags',)
