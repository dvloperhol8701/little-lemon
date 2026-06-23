# update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This includes your specific restaurant app routing rules cleanly
    path('restaurant/', include('restaurant.urls')),
]