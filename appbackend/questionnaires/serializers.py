from django.contrib.auth.models import User, Group
from users.models import Therapist, Client
from users.serializers import TherapistSerializer, ClientSerializer, UserSerializer
from questionnaires.models import Questionnaire, Question, QuestionChoice, QuestionInput, QuestionNumeric, OptionChoice, QuestionNumeric, OptionNumeric, OptionInput, QuestionNumericEntry, QuestionChoiceEntry, QuestionInputEntry, QuestionnaireEntry
from rest_framework import serializers


#class OptionSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Option
   #     fields = ['pk','option_text']

#options serializers
class OptionChoiceSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, queryset=QuestionChoice.objects.all())
    class Meta:
        model = OptionChoice
        fields = ['pk','option_value', 'question']

class OptionInputSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, queryset=QuestionInput.objects.all())
    class Meta:
        model = OptionInput
        fields = ['pk','standard_text', 'question']

class OptionNumericSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, queryset=QuestionNumeric.objects.all())
    class Meta:
        model = OptionNumeric
        fields = ['pk','min_value','max_value', 'question']

#questions serializers
class QuestionSerializer(serializers.ModelSerializer):
    creator = TherapistSerializer(many=False)
    class Meta:
        model = Question
        fields = ['pk','question_text','creator']

#input
class QuestionInputSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    #creator = TherapistSerializer(many=False)
    optioninputs = OptionInputSerializer(many=True, required=False)
    class Meta:
        model = QuestionInput
        fields = ['pk', 'questionnaires', 'question_text','creator','optioninputs']
#choice
class QuestionChoiceSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    #creator = TherapistSerializer(many=False)
    optionchoices = OptionChoiceSerializer(many=True, required=False)
    class Meta:
        model = QuestionChoice
        fields = ['pk','questionnaires','creator','question_text','optionchoices']

class QuestionNumericSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    #creator = TherapistSerializer(many=False)
    optionnumerics = OptionNumericSerializer(many=True, required=False)
    class Meta:
        model = QuestionNumeric
        fields = ['pk', 'questionnaires', 'creator','question_text','optionnumerics']

#question Entry serializers
class QuestionInputEntrySerializer(serializers.ModelSerializer):
    question = QuestionInputSerializer
    creator = ClientSerializer
    class Meta:
        model = QuestionInputEntry
        fields =['pk','creator','questionnaire_entry', 'response_text','entry_date','question']

class QuestionChoiceEntrySerializer(serializers.ModelSerializer):
    question = QuestionChoiceSerializer
    creator = ClientSerializer
    class Meta:
        model = QuestionChoiceEntry
        fields =['pk','creator','questionnaire_entry','choice_value','entry_date','question']

class QuestionNumericEntrySerializer(serializers.ModelSerializer):
    question = QuestionNumericSerializer
    creator = ClientSerializer
    class Meta:
        model = QuestionNumericEntry
        fields =['pk','creator','questionnaire_entry','response_value','entry_date','question']


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
    #creator = TherapistSerializer(many=False)
    inputquestions = QuestionInputSerializer(many=True, required=False)
    choicequestions = QuestionChoiceSerializer(many=True, required=False)
    numericquestions = QuestionNumericSerializer(many=True, required=False)

    class Meta:
        model = Questionnaire
        fields = ['pk','title', 'creator','inputquestions', 'choicequestions', 'numericquestions']


class ClientEntrySerializer(serializers.ModelSerializer):
    user_ref = UserSerializer(many=False)
    thera = TherapistSerializer(many=False)
    choiceentries = QuestionChoiceEntrySerializer(many=True)
    inputentries = QuestionInputEntrySerializer(many=True)
    numericentries = QuestionNumericEntrySerializer(many=True)

    class Meta:
        model = Client
        fields = ['pk','user_ref','thera', 'choiceentries','inputentries','numericentries']

class QuestionnaireEntrySerializer(serializers.ModelSerializer):
    choiceentries = QuestionChoiceEntrySerializer(many=True, required=False)
    inputentries = QuestionInputEntrySerializer(many=True, required=False)
    numericentries = QuestionNumericEntrySerializer(many=True, required=False)

    class Meta:
        model = QuestionnaireEntry
        fields = ['pk','creator','entry_date', 'questionnaire', 'is_completed', 'choiceentries','inputentries','numericentries']
