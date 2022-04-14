from rest_framework import serializers
from .models import Reward

class RewardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'