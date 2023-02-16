
from django.contrib import admin
from django.urls import path,include
from .kaya import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('goel/',test),
    path('emp/',include('emp.urls'))
]
 