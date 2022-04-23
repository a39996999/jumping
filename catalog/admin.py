from django.contrib import admin
from .models import student
from django.contrib.auth.models import User, Group
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
'''
class studentResource(resources.ModelResource):
    school = Field(attribute='school_id', column_name='學校')
    std_No = Field(attribute='std_No', column_name='代號')
    name = Field(attribute='name', column_name='姓名')
    score = Field(attribute='score', column_name='次數')
    class Meta:
       model = student
       #fileds = ('school', 'std_No', 'name', 'score')
       #export_order = ('school', 'std_No', 'name', 'score')
       exclude = ('id')
       skip_unchanged = True
       report_skipped = True
       import_id_fields = ('name', 'std_No')
'''
class studentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('school', 'std_No', 'name', 'score')
    search_fields = ('name',)
    list_filter = ('school',)
    #resource_class = studentResource

# Register your models here.

#admin.site.register(school)
admin.site.register(student, studentAdmin)

#刪除預設欄位
admin.site.unregister(User)  
admin.site.unregister(Group)