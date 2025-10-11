from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Group(models.Model):
    name = models.CharField()


    def __str__(self):
        return f'{self.name} - {self.id}'


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return f'{self.id} - {self.name}'
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        

        

class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя студента')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст студента')
    email = models.EmailField(verbose_name='Электронная почта')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    avatar = models.ImageField(verbose_name='Фото профиля')
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    description = models.TextField(verbose_name='Описание студента')
    join_date = models.DateField(verbose_name='Дата начала обучения', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='Дата обновления', auto_now_add=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    tags = models.ManyToManyField(Tag, related_name="students", verbose_name="теги", blank=True)


    def __str__(self):
        return f'{self.name} - {self.id}'


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя учителя')
    email = models.EmailField(verbose_name='Электронная почта')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    join_date = models.DateField(verbose_name='Дата начала обучения', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='Дата обновления', auto_now_add=True)  


    def __str__(self):
        return f'{self.name} - {self.id}'
    

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


# class StudentTag(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)