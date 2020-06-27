from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Question, Answers
from .serializers import QuestionSerialize, AnswerSerializer
from .form import QuestionForm, AnswerForm
import requests

def question_ask(request):

    if request.method=='POST':
        the_form = QuestionForm(request.POST)
        if the_form.is_valid():
        	form_data = request.POST.copy()
        	data = { 
	        	"name": form_data.get('name'), 
	        	"email": form_data.get('email'), 
	        	"ques": form_data.get('ques'), 
	        	"ques_description": form_data.get('ques_description'),
	        	"answers_given": [],
	        	"notify": True if form_data.get('notify') == 'on' else False
	        	}
	        URL = 'http://127.0.0.1:8000/questions/api/ques/'
	        response = requests.post(URL, json=data)
	        print(response.text)
	        success_msg = "Submitted!"
	        the_form = QuestionForm()

        else:
        	success_msg = "failed to submit"
    else:
        the_form = QuestionForm()
        success_msg = ""
    contxt = {'form': the_form, 'success_msg':success_msg}
    return render(request, 'question_ask.html', contxt)


def question_index(request):
	questions = Question.objects.all().order_by('-asked_on')
	contxt = {'questions': questions}
	return render(request, 'question_index.html', contxt)


def question_details(request, pk, s):
	return render(request, 'question_detail.html')


def answer_index(request, pk, s):
    contxt = {}
 
    if request.method=='POST':
        the_form = AnswerForm(request.POST)
        if the_form.is_valid():
            form_data = request.POST.copy()
            data = {"author":form_data.get('author'),
                    "the_answer": form_data.get('the_answer'),
                    "question" : pk
                    }
            URL = 'http://127.0.0.1:8000/questions/api/answer/'
            response = requests.post(URL, json=data)
            success_msg = "Submitted SuccessFully!"
            contxt['form'] = AnswerForm()
            contxt['success_msg'] = "Submitted Successfully!"

    else:
        contxt['form'] = AnswerForm()

    try:
        URL ='http://127.0.0.1:8000/questions/api/ques/'+str(pk)
        print(URL)
        question = requests.get(url = URL)
        question = question.json()
        print(question)
    except:
        contxt ={'error_message':"No Question with that id"}
        print(contxt['error_message'])
        return render(request, 'question_index.html', contxt)

    contxt['question'] = question['ques']
    contxt['ques_description'] = question['ques_description']
    contxt['the_answers'] = question['answers_given']

 
    return render(request, 'answer_index.html', contxt)





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

@api_view(['GET', 'PUT'])
def get_put_question(request, pk):
    
    try:
        question = Question.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =="GET":
        serial = QuestionSerialize(question)
        return Response(serial.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def answer_list(request):
    # try:
    #     slug = slug.replace('-', ' ')
    #     question = Question.objects.get(pk=pk, ques=slug)
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='GET':
        answers = Answers.objects.all()
        ans = AnswerSerializer(answers, many=True)
        return Response(ans.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        print(request.data.get('name'))

        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            answer = serializer.save()
            serializer = AnswerSerializer(answer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
