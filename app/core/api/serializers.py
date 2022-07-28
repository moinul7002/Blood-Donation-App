from rest_framework import serializers
from core.models import *

class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor
        fields = ('id', 'firstname', 'lastname', 'age', 'sex','location','blood_group')