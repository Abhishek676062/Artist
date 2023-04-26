from django.urls import path
from myapp.views import WorkList, UserCreate
from myapp import views

urlpatterns = [
    path('myapp/works', WorkList.as_view(), name='work_list'),
    path('myapp/register', UserCreate.as_view(), name='register'),
    path('', views.index, name='index'),
]
