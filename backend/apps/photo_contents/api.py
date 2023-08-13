from rest_framework import serializers
from rest_framework.views import APIView, Request, Response

from photo_contents.models import Photo, Tag
from photo_contents.selectors import tags_list
from photo_contents.services.photo_services import photo_detail


class TagListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = ('id', 'slug')

    def get(self, request: Request) -> Response:
        tags = tags_list()
        serializer = self.OutputSerializer(tags, many=True)
        return Response(serializer.data)


class PhotoListApi(APIView):
    class FilterSerializer(serializers.Serializer):
        category = serializers.ListField(
            child=serializers.SlugField(),
            required=False
        )

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Photo
            fields = ('image',)

    def get(self, request: Request) -> Response:
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        photo = photo_detail(filters=filters_serializer.validated_data)
        serializer = self.OutputSerializer(photo)
        return Response(serializer.data)
