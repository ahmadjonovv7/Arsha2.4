from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPort(admin.ModelAdmin):
    list_display = ['id','nomi','comp_name','tur','data','rasm1']

admin.site.register(Portfolio,AdminPort)



class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminTur)


class AdminMsg(admin.ModelAdmin):
    list_display = ['id','ism','pochta','sub','text','data']

admin.site.register(Murojat,AdminMsg)



class AdminTeam(admin.ModelAdmin):
    list_display = ['id','nomi','lavozim','text']

admin.site.register(team,AdminTeam)