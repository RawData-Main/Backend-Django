from django.contrib import admin
from . models import *


# Register your models here.

# admin.site.register(User)
# admin.site.register(Customer)
# admin.site.register(ReportUser)

class UserItemAdmin(admin.ModelAdmin):

    list_display = ['id','username','is_customer','is_report_user']

    def get_form(self, request, obj=None, **kwargs):
        form = super(UserItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['id'].label_from_instance = lambda inst: "{} {}".format(inst.id, inst.username, inst.is_customer, inst.is_report_user)
        return form

admin.site.register(User, UserItemAdmin)


class CustomerItemAdmin(admin.ModelAdmin):

    list_display = ['user','phone','email']

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomerItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].label_from_instance = lambda inst: "{} {}".format(inst.user, inst.phone, inst.email)
        return form

admin.site.register(Customer, CustomerItemAdmin)



class ReportUserItemAdmin(admin.ModelAdmin):

    list_display = ['user','phone','email']

    def get_form(self, request, obj=None, **kwargs):
        form = super(ReportUserItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].label_from_instance = lambda inst: "{} {}".format(inst.user, inst.phone, inst.email)
        return form
        
admin.site.register(ReportUser, ReportUserItemAdmin)
