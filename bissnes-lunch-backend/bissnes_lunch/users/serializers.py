from rest_framework.serializers import ModelSerializer

from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name' ,'surname', 'job_title' ,'email')