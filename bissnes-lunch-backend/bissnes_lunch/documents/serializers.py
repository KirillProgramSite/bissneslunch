from rest_framework.serializers import ModelSerializer

from documents.models import Documents
from users.models import User

from users.serializers import UserSerializer

class DocumentSerializer(ModelSerializer):
    

    class Meta:
        model = Documents
        fields = ('id', 'user', 'type_weekend', 'date_from', 'days_weekend', 'date')