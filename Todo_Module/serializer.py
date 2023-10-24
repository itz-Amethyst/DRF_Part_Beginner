from rest_framework import serializers

from Todo_Module.models import Todo

from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if priority < 10 or priority > 20:
            raise serializers.ValidationError('priority is not between 10 and 20 genius')
        return priority

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # Related name in model
    todos = TodoSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = '__all__'