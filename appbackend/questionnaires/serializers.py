from django.contrib.auth.models import User, Group
from users.models import Therapist, Client
from questionnaires.models import Questionnaire, Question, QuestionEntry
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class TherapistSerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    class Meta:
        model = Therapist
        fields = ['is_therapist', 'user_ref']

class ClientSerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    class Meta:
        model = Client
        fields = ['user_ref']
        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    creator = TherapistSerializer(many=False)
    class Meta:
        model = Question
        fields = ['pk','question_text','creator']

class QuestionEntrySerializer(serializers.ModelSerializer):
    question = QuestionSerializer
    creator = ClientSerializer
    class Meta:
        model = QuestionEntry
        fields =['pk','response_text','entry_date', 'creator']


class QuestionnaireSerializer(serializers.ModelSerializer):
    creator = TherapistSerializer(many=False)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ['title', 'creator','questions']