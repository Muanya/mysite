from django.db import models
from django.template.defaultfilters import slugify

class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    ques = models.CharField(max_length=250)
    ques_slug = models.SlugField(null=False, unique=True) 
    ques_description = models.TextField()
    notify = models.BooleanField(default=False)
    asked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ques


class Answers(models.Model):
	author = models.CharField(max_length=50)
	the_answer = models.TextField()
	answered_on = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_given', blank=True, null=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.the_answer
