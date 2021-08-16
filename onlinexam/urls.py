from django.urls import path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('lecturer/',include('lecturer.urls')),
    path('student/',include('student.urls')),
    


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),



    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='exam/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-lecturer', views.admin_lecturer_view,name='admin-lecturer'),
    path('admin-view-lecturer', views.admin_view_lecturer_view,name='admin-view-lecturer'),
    path('update-lecturer/<int:pk>', views.update_lecturer_view,name='update-lecturer'),
    path('delete-lecturer/<int:pk>', views.delete_lecturer_view,name='delete-lecturer'),
    path('admin-view-pending-lecturer', views.admin_view_pending_lecturer_view,name='admin-view-pending-lecturer'),
    path('admin-view-lecturer-salary', views.admin_view_lecturer_salary_view,name='admin-view-lecturer-salary'),
    path('approve-lecturer/<int:pk>', views.approve_lecturer_view,name='approve-lecturer'),
    path('reject-lecturer/<int:pk>', views.reject_lecturer_view,name='reject-lecturer'),

    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('admin-view-student-marks', views.admin_view_student_marks_view,name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),

    path('admin-course', views.admin_course_view,name='admin-course'),
    path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),


]
