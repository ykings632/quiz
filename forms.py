from django import forms
from stdmanage.models import Questions

class QuestionForm(forms.Form):
    class Meta:
        model = Questions
        fields = ('questions', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_answer')
