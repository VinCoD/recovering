from django.contrib import admin
from .models import Test, New, Relative, Remark
# Register your models here.
admin.site.site_header = "The Continental"
admin.site.register(Test)
admin.site.register(New)
admin.site.register(Relative)
admin.site.register(Remark)

