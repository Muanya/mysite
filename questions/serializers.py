from django.template.defaultfilters import slugify
from rest_framework import serializers, fields
from .models import Question, Answers



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = (
				'author',
				'the_answer',
				'votes',
                'question',
				'answered_on',
			)


class QuestionSerialize(serializers.ModelSerializer):
    answers_given = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('name', 'email', 'ques', 'ques_description', 'asked_on', 'answers_given', "notify")

    def create(self, validated_data):
        answers_data = validated_data.pop('answers_given')
        validated_data['ques_slug'] = slugify(validated_data['ques'])
        question = Question.objects.create(**validated_data)
        for ans in answers_data:
            Answers.objects.create(question=question, **ans)
        return question
    
    def update(self, instance, validated_data):
        # ans_given = validated_data.pop('answers_given')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.ques = validated_data.get('ques', instance.ques)
        instance.ques_slug = slugify(instance.ques)
        instance.notify = validated_data.get('notify', instance.notify)
        instance.ques_description = validated_data.get('ques_description', instance.message)
        instance.save()
        
        return instance