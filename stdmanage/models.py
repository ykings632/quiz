from django.db import models

# Create your models here.

class Questions(models.Model):
    questions = models.CharField(max_length=200, unique=True)
    choice1 = models.CharField(max_length=100, unique=False)
    choice2 = models.CharField(max_length=100, unique=False)
    choice3 = models.CharField(max_length=100, unique=False)
    choice4 = models.CharField(max_length=100, unique=False)
    correct_answer = models.CharField(max_length=100, unique=False)
	

class Results(models.Model):
	result_question = models.CharField(max_length=200)
	result_choice1 = models.CharField(max_length=100)
	result_choice2 = models.CharField(max_length=100)
	result_choice3 = models.CharField(max_length=100)
	result_choice4 = models.CharField(max_length=100)
	result_correct_answer = models.CharField(max_length=100)
	result_choose_correct = models.CharField(max_length=100)
	result_user_id = models.CharField(max_length=100)
	result_exam_date = models.DateTimeField(auto_now_add=True)