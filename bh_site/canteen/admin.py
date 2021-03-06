from django.contrib import admin
from guardian.admin import GuardedModelAdmin
# Register your models here.
from .models import *



from .models import CanteenModel

class CanteenModerator(GuardedModelAdmin):
    pass

admin.site.register(CanteenModel, CanteenModerator)
admin.site.register(DishModel)
admin.site.register(CategoryModel)
