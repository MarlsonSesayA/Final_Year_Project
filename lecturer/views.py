from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from student import models as SMODEL
from exam import forms as QFORM


def lecturerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'lecturer/lecturerclick.html')

def lecturer_signup_view(request):
    userForm=forms.LecturerUserForm()
    lecturerForm=forms.LecturerForm()
    mydict={'userForm':userForm,'lecturerForm':lecturerForm}
    if request.method=='POST':
        userForm=forms.LecturerUserForm(request.POST)
        lecturerForm=forms.LecturerForm(request.POST,request.FILES)
        if userForm.is_valid() and lecturerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            lecturer=lecturerForm.save(commit=False)
            lecturer.user=user
            lecturer.save()
            my_lecturer_group = Group.objects.get_or_create(name='LECTURER')
            my_lecturer_group[0].user_set.add(user)
        return HttpResponseRedirect('lecturerlogin')
    return render(request,'lecturer/lecturersignup.html',context=mydict)



def is_lecturer(user):
    return user.groups.filter(name='LECTURER').exists()

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_student':SMODEL.Student.objects.all().count()
    }
    return render(request,'lecturer/lecturer_dashboard.html',context=dict)

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_exam_view(request):
    return render(request,'lecturer/lecturer_exam.html')


@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/lecturer/lecturer-view-exam')
    return render(request,'lecturer/lecturer_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'lecturer/lecturer_view_exam.html',{'courses':courses})

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/lecturer/lecturer-view-exam')

@login_required(login_url='adminlogin')
def lecturer_question_view(request):
    return render(request,'lecturer/lecturer_question.html')

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/lecturer/lecturer-view-question')
    return render(request,'lecturer/lecturer_add_question.html',{'questionForm':questionForm})

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def lecturer_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'lecturer/lecturer_view_question.html',{'courses':courses})

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'lecturer/see_question.html',{'questions':questions})

@login_required(login_url='lecturerlogin')
@user_passes_test(is_lecturer)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/lecturer/lecturer-view-question')
