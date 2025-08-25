from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *

admin.site.register(CustomUser)