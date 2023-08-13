from django.urls import include, path

from photo_contents.api import PhotoListApi, TagListApi

tag_patterns = [
    path('', TagListApi.as_view(), name='list'),
]

photo_patterns = [
    path('', PhotoListApi.as_view(), name='list'),
]

urlpatterns = [
    path('tags/', include((tag_patterns, 'tags'))),
    path('photo/', include((photo_patterns, 'photos'))),
]
