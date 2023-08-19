from django.contrib import admin
from myadmin.models import Notice

admin.site.site_header = 'Notice Hub Web App'
admin.site.index_title = 'My Admin Panel'

class NoticeAdmin(admin.ModelAdmin):
	list_display = ['id','subject','description','created_at','updated_at']


admin.site.register(Notice, NoticeAdmin)

