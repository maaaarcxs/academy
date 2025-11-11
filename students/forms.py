from django import forms
from phonenumber_field import phonenumber
from students.models import Student, Group, Tag

class StudentForm(forms.Form):
    name = forms.CharField(label="Имя студента", widget=forms.TextInput(attrs={"class" : "student_input student_input2", }))
    last_name = forms.CharField(label="Фамилия студента")
    age = forms.IntegerField(label="Возраст студента")
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={"class" : "student_input student_input2", }))
    phone_number = forms.CharField(label="Номер телефона")
    group = forms.ModelChoiceField(label="Группа", queryset=Group.objects.all())
    picture = forms.ImageField(label="Фото профиля", required=False)
    join_date = forms.DateField(label="Дата присоединения: ")
    updated_time = forms.DateTimeField(label="Дата обновления")
    is_active = forms.BooleanField(label="Активен", required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "last_name", "age", "email", "phone_number", "group", "avatar", "is_active", "tags")
        labels = {
            "name": "Имя студента",
            "last_name" : "Фамилия студента",
            "age": "Возраст студента",
            "email": "Электронная почта",
            "phone_number": "Номер телефона",
            "group": "Группа",
            "avatar": "Фото профиля",
            "is_active": "Активен",
            "tags": "теги"
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "student_input"}),
            "last_name" : forms.TextInput(attrs={"class" : "student_input"}),
            "age": forms.NumberInput(attrs={"class" : "student_input"}),
            "email": forms.EmailInput(attrs={"class" : "student_input"}),
            "phone_number": forms.NumberInput(attrs={"class" : "student_input"}),
            "group": forms.Select(attrs={"class" : "student_input"}),
            "avatar": forms.ClearableFileInput(attrs={"class" : "student_input"}),
            "is_active": forms.CheckboxInput(attrs={"class" : "student_input"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "student_input"})
        }