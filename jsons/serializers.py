from rest_framework import serializers
from .models import Giftshop

class GiftshopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Giftshop
		fields = '__all__'
