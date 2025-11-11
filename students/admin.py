from django.contrib import admin

from .models import Student, Group, Teacher, Tag, StudentContract



class StudentContractAdmin(admin.ModelAdmin):
    list_display = ('student__name', "balance", "student__join_date")
    search_fields = ('student__name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'email', 'group__name')
    list_filter = ('group__name', 'age', 'tags__name')
    ordering = ('-join_date', '-updated_date')
    # list_editable = ("phone_number", 'email')
    readonly_fields = ('join_date', 'updated_date') 
    filter_horizontal = ("tags", )
    # list_select_related = ("tags")
    # raw_id_fields = ("tags",)
    # list_per_page = 100
    # fieldsets = (
    #     ('Основная информация', {
    #         'fields': ('name', 'last_name', 'age', 'email', 'phone_number', 'group', 'avatar', )
    #     }),
    #     ('Дополнительная информация', {
    #         'fields': ('join_date', 'updated_date'),    
    #         'classes': ('collapse',)
    #     }),
    # )
    # prepopulated_fields = {'last_name': ('name',)}
    date_hierarchy = 'join_date'
    # fields = ('name', 'email', 'last_name')
    exclude = ("last_name",)
    save_on_top = True

    @admin.action(description="Активировать пользователей")
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    actions = [make_active]


class GroupAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentContract, StudentContractAdmin)
