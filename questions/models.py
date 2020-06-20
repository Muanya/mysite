from django.db import models

class Question(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=150)
	message = models.TextField()
	asked_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message


class Answers(models.Model):
	author = models.CharField(max_length=50)
	the_answer = models.TextField()
	answered_on = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_given', blank=True, null=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.the_answer