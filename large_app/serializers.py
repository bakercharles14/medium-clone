from rest_framework import serializers

from .models import User, Post, Comment, Clap


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):
    claps = ClapSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'article',
                  'image_url',
                  'tags'
                  'claps'
                  'comments'
                  'user'
                  )
