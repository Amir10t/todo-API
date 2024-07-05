from rest_framework.serializers import ModelSerializer
from todo.models import TodoModel, User


class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'

class UserSerializer(ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'