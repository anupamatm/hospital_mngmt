from django.contrib import admin

from .models import Department,Doctor,AdminLogin,Staff

# Register your models here.


admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(AdminLogin)
admin.site.register(Staff)