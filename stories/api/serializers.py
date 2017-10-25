from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from accounts.api.serializers import UserDetailSerializer
from stories.models import Story


class StoryListerializer(ModelSerializer):
    user=UserDetailSerializer(read_only=True)

    class Meta:
        model = Story
        fields = ['title',
                  'content',
                  'user',
                  'publish',
                  'image',
                  ]

#task serializer
class StoryCreateSerializer(ModelSerializer):


    class Meta:
        model = Story
        fields = [
            'title',
            'content',
            'user',
            'publish',
            'image',
        ]



class StoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'content', 'user']


class StoryUpdateSerializer(ModelSerializer):

    class Meta:
        model = Story
        fields = ['title', 'content','user']


class StoryDeleteSerializer(ModelSerializer):

    class Meta:
        model = Story
        fields = ['title', 'content','user']


class PhotoSerializer(HyperlinkedModelSerializer):
    class Meta:
       model=Story,
       fields=['title','content','image']