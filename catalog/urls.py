from django.contrib import admin
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
