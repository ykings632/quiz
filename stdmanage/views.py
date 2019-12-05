from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from stdmanage.models import Questions
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def index(request):
      
      return render(request, 'index.html')
      
def register(request):
      if request.method == 'POST':
            
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            password1=request.POST['password1']
            password2=request.POST['password2']
            if password1==password2:
                  if User.objects.filter(username=username).exists():
                        messages.error(request,'Username Taken')
                        return redirect('register')
                  elif User.objects.filter(email=email).exists():
                        messages.error(request,"Email Already Exists")
                        return redirect('register')
                  else:     
                        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)	
                        user.save();
                        messages.success(request,'Account Created Successfully')
                        return redirect('login')
            else:
                  messages.error(request,'Password And Confirm-Password Not Matching')
                  return redirect('register')
      else:
            return render(request, 'register.html')
      
def login(request):
      if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                  auth.login(request,user)
                  return redirect('dashboard')
            else:
                  messages.error(request,'Invalid Login Details')
                  return redirect('login')    
      else:      
           return render(request, 'login.html')


def dashboard(request):
      if request.session._session:
            return render(request, 'dashboard.html') 
      else:
            return render(request, 'login.html')       

def manage_question(request):
      if request.session._session:
            questions = Questions.objects.all()
            return render(request, 'manage-question.html',{'Questions':questions})
      else:
            return render(request, 'login.html') 

def manage_student(request):
      if request.session._session:
            users=User.objects.all()
            return render(request, 'manage-student.html',{'users':users})
      else:
            return render(request, 'login.html')

def quiz_test(request):
      if request.session._session:
            questions= Questions.objects.all()
            count= Questions.objects.all().count()
            return render(request,'quiz-test.html',{'questions':questions,'count':count})
      else:
            return render(request, 'login.html')

def quiz_result(request):
      if request.session._session:
            return render(request,'quiz-result.html')
      else:
            return render(request, 'login.html')

# def change_password(request):
#       if request.session._session:
#             return render(request, 'change-password.html')    
#       else:
#             return render(request, 'login.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })
 
def add_question(request):
      if request.session._session:
            return render(request, 'add-question.html')    
      else:
            return render(request, 'login.html')


def add_question_data(request):
      
      if request.method == 'POST':
            question=request.POST['questions']
            choice1=request.POST['choice1']
            choice2=request.POST['choice2']
            choice3=request.POST['choice3']
            choice4=request.POST['choice4']
            correct_answer=request.POST['right_answer']
            questions_data= Questions(questions=question,choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=correct_answer)
            questions_data.save();
            messages.success(request,'Question Added Successfully')
            return render(request, 'add-question.html')  
      else:
            return render(request, 'add-question.html')

def  delete_question(request, pk):
      Questions.objects.filter(id=pk).delete()
      messages.success(request,'Questions Deleted Successfully')
      return redirect('manage_question')

def  delete_student(request, pk):
      User.objects.filter(id=pk).delete()
      messages.success(request,'Student Record Deleted Successfully')
      return redirect('manage_student')  

def edit_question(request, pk):
      item = Questions.objects.filter(id=pk).values()
      return render(request, 'edit-question.html', {'data':item})


def logout(request):
      auth.logout(request)
      return redirect('/')

def update_question_data(request):
      if request.method == "POST":
            question_id=request.POST['question_id']
            question_data = Questions.objects.get(id=question_id)
            question_data.questions = request.POST['questions']
            question_data.choice1 = request.POST['choice1']
            question_data.choice2 = request.POST['choice2']
            question_data.choice3 = request.POST['choice3']
            question_data.choice4 = request.POST['choice4']
            question_data.correct_answer = request.POST['right_answer']
            question_data.save();
            messages.success(request,'Questions Updaded Successfully')
            return redirect('manage_question')
      else:
            return redirect('manage_question')

def update_question_data(request):
      if request.method == "POST":
            question_id=request.POST['question_id']
            question_data = Questions.objects.get(id=question_id)
            question_data.questions = request.POST['questions']
            question_data.choice1 = request.POST['choice1']
            question_data.choice2 = request.POST['choice2']
            question_data.choice3 = request.POST['choice3']
            question_data.choice4 = request.POST['choice4']
            question_data.correct_answer = request.POST['right_answer']
            question_data.save();
            messages.success(request,'Questions Updaded Successfully')
            return redirect('manage_question')
      else:
            return redirect('manage_question')

def result(request):
            values = list(request.POST)
            keys = list(request.POST.items())
            n=1
            right_answer = []
            unanswered = 0
            wrong_answer = 0
            newlist = values[n:] 
            values_data = Questions.objects.filter(pk__in = newlist).values().order_by('id')
            return render(request,'result.html',{'value':values_data,'answer':keys,'right_answer':right_answer,'unanswered':unanswered,'wrong_answer':wrong_answer})
            # keys = list(request.POST.items())
            # n = 1
            # newlist = values[n:]
            # values_data = Questions.objects.filter(pk__in = newlist).values().order_by('id')
            # values_data=list(values_data)
            # return render(request,'result.html',{'value':values_data,'answer':keys})