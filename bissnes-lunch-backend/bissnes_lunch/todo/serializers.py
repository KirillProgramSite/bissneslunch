from rest_framework.serializers import ModelSerializer

from todo.models import Todo
from users.models import User
from users.serializers import UserSerializer

class TodoSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'description', 'completed')


        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = User.objects.get_or_create(**user_data)
            todo = Todo.objects.create(user=user, **validated_data)
            return todo