from rest_framework import serializers, fields
from .models import Question, Answers


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answers
		fields = (
				'author',
				'the_answer',
				'votes',
				'answered_on',
			)


class QuestionSerialize(serializers.ModelSerializer):
	answers_given = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = ('name', 'email', 'message', 'asked_on', 'answers_given')

	def create(self, validated_data):
		answers_data = validated_data.pop('answers_given')
		question = Question.objects.create(**validated_data)
		ans_serializer = self.fields['answers_given']
		for ans in answers_data:
			ans['question'] = question
		answer = ans_serializer.create(answers_data)
		return question