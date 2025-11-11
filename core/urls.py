"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students.views import main, student_details, create_student, student_update, student_delete, student_details, StudentView, StudentDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", StudentView.as_view(), name='main'),
    # path('', main, name='main'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='students_details'),
    path('create-student/', create_student, name='create_student'),
    path('students/<int:id>/update/', student_update, name='student_update'),
    path('students/<int:id>/delete/', student_delete, name='student_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)