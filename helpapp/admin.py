from django.contrib import admin
from helpapp.models import AccessRecord,Topic,Webpage

class helpAdmin(admin.ModelAdmin):
    fields=['topic','name','url']

    def __init__(self, arg):
        super(helpAdmin, self).__init__()
        self.arg = arg

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
