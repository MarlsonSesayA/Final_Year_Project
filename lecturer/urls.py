from django.urls import path
from lecturer import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('lecturerclick', views.lecturerclick_view),
path('lecturerlogin', LoginView.as_view(template_name='lecturer/lecturerlogin.html'),name='lecturerlogin'),
path('lecturersignup', views.lecturer_signup_view,name='lecturersignup'),
path('lecturer-dashboard', views.lecturer_dashboard_view,name='lecturer-dashboard'),
path('lecturer-exam', views.lecturer_exam_view,name='lecturer-exam'),
path('lecturer-add-exam', views.lecturer_add_exam_view,name='lecturer-add-exam'),
path('lecturer-view-exam', views.lecturer_view_exam_view,name='lecturer-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('lecturer-question', views.lecturer_question_view,name='lecturer-question'),
path('lecturer-add-question', views.lecturer_add_question_view,name='lecturer-add-question'),
path('lecturer-view-question', views.lecturer_view_question_view,name='lecturer-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]