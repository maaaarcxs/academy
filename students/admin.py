from django.contrib import admin

from .models import Student, Group, Teacher, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = {"id", "name"}
    list_display_links = {"id", "name"}
    search_fields = {"name", "id"}

class GroupAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'age', 'email', 'phone_number', 'group')
    list_display_links = ('id', 'name')
    list_editable = ('phone_number', 'age')
    search_fields = ('name', 'email', 'group', 'phone_number', 'group')
    list_filter = ('group', 'age')
    ordering = ('-join_date', '-update_time')
    readonly_fields = ('join_date', 'update_time')
    list_per_page = 3
    fieldsets = (
        ('Основная информация', {
            "fields": ('name', 'last_name', 'age', 'email', 'phone_number', 'group', 'avatar'),
        }),

        ('Дополнительная информация', {
            'fields': ('join_date', 'update_time'),
            'classes': ('collapse',)
        })
    )
    # prepopulated_fields = {'last_name': ('name',)}
    # date_hierarchy = 'join_date'
    # fields = ('name', 'email', 'last_name')
    # exclude = ['last_name']
    # save_on_top=True
    


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Teacher, TeacherAdmin)