from django.contrib import admin
from .models import *  # TestOlymp

# Register your models here.
admin.site.register(QMapping)
admin.site.register(QUniversuty)
admin.site.register(QFaculty)
admin.site.register(QOlymp)
admin.site.register(QPrivilege)
admin.site.register(QSubject)



