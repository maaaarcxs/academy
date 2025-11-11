import django_filters
from django import forms

from .models import Student, Group, Tag


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Имя студента")
    group = django_filters.ModelChoiceFilter(
        queryset=Group.objects.all(), 
        widget=forms.Select,
        empty_label="choose"
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = ("name", "age", 'group')