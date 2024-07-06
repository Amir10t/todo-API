from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from todo.models import TodoModel, User


class TodoSerializer(ModelSerializer):
    def validate_priority(self, priority):
        if priority <= 0 or priority > 4:
            raise serializers.ValidationError("It must be between 1 and 4")
        return priority

    class Meta:
        model = TodoModel
        fields = '__all__'

class UserSerializer(ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'