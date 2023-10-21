from rest_framework import serializers

from API.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'is_enable', 'publish_date']