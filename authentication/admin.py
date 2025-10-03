from django.contrib import admin
from .models import Countries, Department, Cities, User
# Register your models here.

#admin.site.register(Countries)
admin.site.register(Department)
admin.site.register(Cities)
admin.site.register(User)

@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev', 'get_status')

    def get_status(self,obj):
        return 'Activate' if self.satatus else 'inactive'
    get_status.shortdescription = 'Status' 