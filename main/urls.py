
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('olamundo/', include('app01.urls')),
    path('livros/', include('app02.urls')),
    path('produtos/', include('cadastrop.urls')),
]