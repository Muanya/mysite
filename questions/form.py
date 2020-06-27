from django import forms

class QuestionForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Your Name'
                                        }))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Your E-mail'
                                        }))
    ques = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Your Question'
                                        }))
    ques_description = forms.CharField(widget=forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Question Desctiption/Detail'
                                        }))
    notify = forms.BooleanField( widget=forms.CheckboxInput(), initial=True, required=False)

    

class AnswerForm(forms.Form):
    author =   forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Your Name'
                                        }))
    the_answer =  forms.CharField(widget=forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Your Answer'
                                        }))
    
    
