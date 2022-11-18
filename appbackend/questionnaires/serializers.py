from django.contrib.auth.models import User, Group
from users.models import Therapist, Client
from questionnaires.models import Questionnaire, Question, QuestionChoice, QuestionInput, QuestionNumeric, OptionChoice, QuestionNumeric, OptionNumeric, OptionInput, QuestionNumericEntry, QuestionChoiceEntry, QuestionInputEntry
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
    creator = UserSerializer(many=False)
    thera = TherapistSerializer(many=False)
    
    class Meta:
        model = Client
        fields = ['creator','thera']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



#class OptionSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Option
   #     fields = ['pk','option_text']

#options serializers
class OptionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionChoice
        fields = ['pk','option_value']

class OptionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionInput
        fields = ['pk','standard_text']

class OptionNumericSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionNumeric
        fields = ['pk','min_value','max_value']

#questions serializers
class QuestionSerializer(serializers.ModelSerializer):
    creator = TherapistSerializer(many=False)
    class Meta:
        model = Question
        fields = ['pk','question_text','creator']

#input
class QuestionInputSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    creator = TherapistSerializer(many=False)
    optioninputs = OptionInputSerializer(many=True)
    class Meta:
        model = QuestionInput
        fields = ['pk','question_text','creator','optioninputs']
#choice
class QuestionChoiceSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    creator = TherapistSerializer(many=False)
    optionchoices = OptionChoiceSerializer(many=True)
    class Meta:
        model = QuestionChoice
        fields = ['pk','creator','question_text', 'optionchoices',]

class QuestionNumericSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    creator = TherapistSerializer(many=False)
    optionnumerics = OptionNumericSerializer(many=True)
    class Meta:
        model = QuestionNumeric
        fields = ['pk','creator','question_text','optionnumerics']

#question Entry serializers
class QuestionInputEntrySerializer(serializers.ModelSerializer):
    question = QuestionInputSerializer(many=False)
    creator = ClientSerializer
    class Meta:
        model = QuestionInputEntry
        fields =['pk','creator','response_text','entry_date','question']

class QuestionChoiceEntrySerializer(serializers.ModelSerializer):
    question = QuestionChoiceSerializer(many=False)
    creator = ClientSerializer
    class Meta:
        model = QuestionChoiceEntry
        fields =['pk','creator','choice_value','entry_date','question']

class QuestionNumericEntrySerializer(serializers.ModelSerializer):
    question = QuestionNumericSerializer(many=False)
    creator = ClientSerializer
    class Meta:
        model = QuestionNumericEntry
        fields =['pk','creator','response_value','entry_date','question']


class QuestionEntrySerializer(serializers.ModelSerializer):
    choiceentries = QuestionChoiceSerializer
    inputentries = QuestionInputEntrySerializer
    numericentries = QuestionNumericEntrySerializer
    creator = ClientSerializer
    class Meta:
        model = QuestionNumericEntry
        fields =['pk','creator','choiceentries','inputentries','numericentries']


#questionnaire serializer
class QuestionnaireSerializer(serializers.ModelSerializer):
    creator = TherapistSerializer(many=False)
    inputquestions = QuestionInputSerializer(many=True)
    choicequestions = QuestionChoiceSerializer(many=True)
    numericquestions = QuestionNumericSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ['title', 'creator','inputquestions', 'choicequestions', 'numericquestions']


class ClientEntrySerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    thera = TherapistSerializer(many=False)
    choiceentries = QuestionChoiceEntrySerializer(many=True)
    inputentries = QuestionInputEntrySerializer(many=True)
    numericentries = QuestionNumericEntrySerializer(many=True)

    class Meta:
        model = Client
        fields = ['user_ref','thera', 'choiceentries','inputentries','numericentries']
