from rest_framework import serializers
from .models import TreasuryYields

class TreasuryYieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreasuryYields
        fields = '__all__'
