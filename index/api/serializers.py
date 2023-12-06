from rest_framework import serializers
from index.models import Palindroma


class PalindromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palindroma
        fields = ('id', 'palabra')
