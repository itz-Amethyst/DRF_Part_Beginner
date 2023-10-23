from rest_framework import serializers

from Todo_Module.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'content']