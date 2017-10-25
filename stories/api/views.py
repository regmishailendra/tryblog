import base64

import data as data
from django.contrib.sites import requests
from django.core.files.base import ContentFile
from django.db.migrations import serializer
from rest_framework import permissions, request, status

from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.parsers import FileUploadParser, JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from stories.api.serializers import StoryListerializer, StoryCreateSerializer, StoryDetailSerializer, \
    StoryUpdateSerializer, PhotoSerializer
from stories.forms import StoryForm
from stories.models import Story
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class StoryListAPIView(ListAPIView):
    serializer_class = StoryListerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Story.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)

            ).distinct()

        return queryset

        # def get(self, request, format=None):
        #     content = {
        #         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        #         'auth': unicode(request.auth),  # None
        #     }


class StoryCreateAPIView(CreateAPIView):
    print("create method")

    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
  #  permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        print('hello'+title+" "+content)

        serializer.save(user=self.request.user)





class StoryDetailAPIView(RetrieveAPIView):  # done
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    permission_classes = [IsAuthenticated]


class StoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryUpdateSerializer

    # permission_classes = [IsAuthenticated]


    def perform_update(self, serializer):

        if serializer.is_valid():
            print('valid data')
            instance = serializer.validated_data
            print(instance.get('user'))
            print(self.request.user)

            if instance.get('user') == self.request.user:
                serializer.save()

            else:
                raise ValidationError('This is not your post.')
        else:
            print('This is not valid data')
            # raise ValidationError('This is not your post')

    print('sdfdsfdsf')


class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryUpdateSerializer

    # permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise ValidationError('You cannot delete this post.')

# class ImageApiView(APIView):
#     def put(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         serializer = PhotoSerializer(photo, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
