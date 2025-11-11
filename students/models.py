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
        return f'{self.name} - {self.id}'
    

class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя студента')
    last_name = models.CharField(max_length=150, null=True, blank=True)
    age = models.IntegerField(verbose_name='Возраст студента', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа', related_name="students")
    avatar = models.ImageField(null=True, blank=True, verbose_name='Аватарка', upload_to='studentsAvatars/')
    phone_number = PhoneNumberField(verbose_name='Номер телефона', null=True, blank=True)
    join_date = models.DateField(verbose_name='дата присоединения', auto_now_add=True)
    updated_date= models.DateTimeField(verbose_name='дата обновления', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    tags = models.ManyToManyField(Tag, related_name='students', verbose_name='теги', blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.name} - {self.group.name}'
    

class StudentContract(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='contract')
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Баланс', )

    def __str__(self):
        return f'Contract for {self.student.name}, balance: {self.balance}'
    
    class Meta:
        verbose_name = "Контракт для студента"
        verbose_name_plural = 'Контракты для студентов'
    
    
# class StudentTag(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)



    

class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя преподавателя') 
    avatar = models.ImageField(null=True, blank=True, verbose_name='Аватарка', upload_to='teachersAvatars/')
    phone_number = PhoneNumberField(verbose_name='Номер телефона') 
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'