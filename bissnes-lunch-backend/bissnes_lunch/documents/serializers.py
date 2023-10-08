from rest_framework.serializers import ModelSerializer

from documents.models import Documents
from users.serializers import UserSerializer

class DocumentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Documents
        fields = ('id', 'user', 'type_weekend', 'date_from', 'days_weekend', 'date')