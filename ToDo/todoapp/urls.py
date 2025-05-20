
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.signup),
    path('loginn/',views.loginn),
    path('todo/',views.todo),
    path('edit_todo/<int:srno>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:srno>',views.delete_todo,name='delete_todo'),
    path('signout/',views.signout,name='signout'),
]
