from django.urls import path

from. import views

urlpatterns=[
    
    path('',views.index, name='index'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('manage_question',views.manage_question,name='manage_question'),
    path('manage_student',views.manage_student,name='manage_student'),
    path('quiz_test', views.quiz_test,name='quiz_test'),
    path('quiz_result', views.quiz_result,name='quiz_result'),
    path('change_password',views.change_password,name='change_password'),
    path('logout', views.logout,name='logout'),
    path('add_question', views.add_question,name='add_question'),
	path('add_question_data',views.add_question_data,name='add_question_data'),
    path('delete_question/<pk>', views.delete_question, name='delete_question'),
    path('delete_student/<pk>', views.delete_student, name='delete_student'),
    path('edit_question/<pk>', views.edit_question, name='edit_question'),
    path('update_question_data',views.update_question_data,name='update_question_data'),
    path('result',views.result,name='result'),
]