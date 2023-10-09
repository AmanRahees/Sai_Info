from django.urls import path
from base.views import *

urlpatterns = [
    path('register', UserRegister, name="user-register"),
    path('login', UserLogin, name="user-login"),
    path('logout', UserLogout, name="user-logout"),
    
    path('', main, name="main"),
    path('add-task', AddTask, name="add-task"),
    path('edit-task/<int:id>', EditTask, name="edit-task"),
    path('delete-task/<int:id>', DeleteTask, name="delete-task"),
    path('complete-task/<int:id>', TaskComplete, name="complete-task"),
]