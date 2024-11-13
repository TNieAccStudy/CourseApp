from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db.models import Count
from django.template.response import TemplateResponse

from courses.models import Category, Course, Lesson,CourseSpecial
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['avatar']
    form = LessonForm

    def avatar(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }

class MyAdminSite(admin.AdminSite):
    index_title = "WELCOME TO ADMIN SITE"

    def get_urls(self):
        return [path('stats/',self.get_stats)] + super().get_urls()

    def get_stats(self,request):
        stats_sql = Category.objects.annotate(count=Count('course__id')).values('id','name','count')
        return TemplateResponse(request,
                                'admin/site_stats.html',
                                {'stats':stats_sql})

admin_site = MyAdminSite('courseapp')

admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(CourseSpecial)
