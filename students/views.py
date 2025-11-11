from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from .forms import StudentForm, StudentModelForm
from .filters import StudentFilter
from django.views import View
from students.models import Student, Group
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


def get_Session_view(request):
    request.session["username"] = "Marcus"


def login_customs(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main')
    else:
        messages.error(request, 'Пользователь не найден или не верный пароль')

    return render(request, 'login.html')


class AboutTemplateView(TemplateView):
    template_name = 'aboutIT/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About page"
        return context

class MainTemplateView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        context["title"] = "Main Page"
        print(context)


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'main.html', {'students': students})
    

    # def post(self, request):
    #     name = request.POST.get("name")
    #     last_name = request.POST.get("last_name")
    #     age = request.POST.get("age", 21)
    #     phone_number = request.POST.get("phone_number", "+996706546483")
    #     email = request.POST.get("email")
    #     Student.objects.create(name = name)
    #     return render(request, "student_create.html")


class StudentDetailView(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        return render(request, 'student_dtls.html', {'student' : student})
    

class StudentCreateView(View):
    model = Student
    template_name = 'create_student.html'
    form_class = StudentModelForm


def main(request):
    students = Student.objects.all()

    search = request.GET.get("search")
    print(search)
    if search:
        students = Student.objects.filter(name__icontains=search)

    filter_set = StudentFilter(request.GET, queryset=students)

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 2)

    paginator = Paginator(filter_set.qs, limit)
    students = paginator.get_page(page)



    return render(request, 'main.html', {
        'students': students,
        'is_paginated': students.has_other_pages(),
        'search' : search,
        'filter' : filter_set
        })


def student_details(request, id):
    student = Student.objects.get(id=id)

    return render(request, 'student_dtls.html', {'student' : student})


def aboutIT(request):

    return render(request, 'aboutIT/index.html')


def create_student(request):
    groups = Group.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            # print("Post request")
            # form = form.cleaned_data
            # print(form)
            form.save()
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        group_id = request.POST.get('group')
        group = Group.objects.get(id=group_id)

        Student.objects.create(
            name=form.get("name"),
            last_name = form.get("last_name"),
            age = form.get("age"),
            phone_number = form.get("phone_number"),
            email = form.get("email"),
            group = form.get("group"),
        )

        form.save()
    #     print("worked")
    # print("Post method!")
        print(request.POST, type(request.POST))
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age", 21)
        phone_number = request.POST.get("phone_number", "+996706546483")
        email = request.POST.get("email", "maaaarcusmoraes@gmail.com")
        group = int(request.POST.get("group", 1))
        picture = request.FILES.get("picture", None)
        print(picture)
        print(group, type(group))
    
        if picture:
            newImageSystem = FileSystemStorage('media/studentsPictures/')
            newImageSystem.save(picture.name, picture)

        Student.objects.create(
        name = name,
        last_name = last_name,
        age = age,
        phone_number = phone_number,
        email = email,
        group_id = group_id,
        picture = picture,
    )
        return redirect('main')
    return render(request, 'create_student.html', context={'form': form, 'groups':groups, 'button_text' : 'Создать'})


def student_update(request, id):
    groups = Group.objects.all()
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_last_name = request.POST.get('last_name')
        new_age = int(request.POST.get('age'))
        new_phone_number = request.POST.get('phone_number')
        new_email = request.POST.get('email')
        new_group = request.POST.get('group')
        new_avatar = request.FILES.get('avatar')

        student.name = new_name
        student.last_name = new_last_name
        student.age = new_age
        student.phone_number = new_phone_number
        student.email = new_email
        student.avatar = new_avatar
        
        if new_avatar:
            student.avatar = new_avatar


        if new_group:
            student.group = Group.objects.get(id=int(new_group))

        # print(request.POST.get('group'))
        # group = Group.objects.get(id=int(request.POST.get('group')))
        # student.group = group

        student.save()
        return redirect('main')

    return render(request, 'student_update.html', {'student':student, 'groups':groups, 'button_text' : 'Изменить'})
    

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('main')