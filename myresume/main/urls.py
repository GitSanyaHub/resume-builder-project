from django.conf.urls.static import static
from django.urls import path
from main import views
from main.views import ResumeDetail, UpdateResumeView
from myresume import settings

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('resume-detail/<int:pk>/', ResumeDetail.as_view(), name='resume-detail'),
    path('create_resume/<int:pk>', UpdateResumeView.as_view(), name='create_resume'),
    path('pdf/', views.pdf, name='pdf')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)