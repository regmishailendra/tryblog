from rest_framework.serializers import ModelSerializer

from accounts.api.serializers import UserDetailSerializer
from stories.models import Story


class StoryListerializer(ModelSerializer):
  #  user=UserDetailSerializer(read_only=True)

    class Meta:
        model = Story
        fields = ['title',
                  'content',
                  #'user',
                  'publish',
                  ]


class StoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'title',
            'content',
            'user',
            'publish',
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
