from backend_dj.src.myJournal.models import bulletJournal
from rest_framework import serializers
from rest_framework.utils import field_mapping

class bulletJSerialzer(serializers.ModelSerializer):
    class Meta:
        model = bulletJournal
        fields=('title','content')