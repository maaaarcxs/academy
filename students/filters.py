import django_filters

from .models import Student, Group, Tag
from django import forms

class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains",  label="Имя студента")
    group = django_filters.ModelChoiceFilter(
        queryset = Group.objects.all(),
        widget = forms.Select,
        empty_label = "choose"
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset = Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )


    class Meta:
        model = Student
        fields = ("name",)