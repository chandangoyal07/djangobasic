from django.urls import path
from . import views


urlpatterns =[
    path('home/',views.emp_home),
    path('add-emp/',views.add_emp),
    path('delete-emp/<int:emp_id>',views.delete_emp),
] 