from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Question, Answers
from .serializers import QuestionSerialize, AnswerSerializer


@api_view(['GET', 'POST'])
def question_list(request):
	if request.method=='GET':
		questions = Question.objects.all()
		serializer = QuestionSerialize(questions, many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		serializer = QuestionSerialize(data=request.data)
		if serializer.is_valid():
			question = serializer.save()
			serializer = QuestionSerialize(question)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
