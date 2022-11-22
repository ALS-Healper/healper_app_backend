from django.contrib.auth.models import User, Group
from users.models import Therapist, Client
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email']

class TherapistSerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    class Meta:
        model = Therapist
        fields = ['pk','is_therapist', 'user_ref']

class ClientSerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    thera = TherapistSerializer(many=False)
    
    class Meta:
        model = Client
        fields = ['user_ref', 'thera']

class UserDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=True)
    therapist = TherapistSerializer(many=True)

    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name','email', 'client', 'therapist']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClientListSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True)
    class Meta:
        model = Therapist
        fields = ['clients']
