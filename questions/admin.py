from django.contrib import admin
from .models import Answers, Question
# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
	list_display = ('author', 'the_answer')

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'ques')

admin.site.register(Answers, AnswersAdmin)
admin.site.register(Question, QuestionAdmin)