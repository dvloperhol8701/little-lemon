from django.contrib import admin
from django.urls import path, include
from rest_framework import routers        # <-- Step 4: Import DRF routers
from restaurant import views              # <-- Import your restaurant views

# Step 4: Create a router and register the BookingViewSet
router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Keeps your existing menu and user endpoints active
    path('restaurant/', include('restaurant.urls')), 
    
    # Step 4: Include the router-generated booking URLs
    path('restaurant/booking/', include(router.urls)),


# ─── ADD THESE TWO LINES FOR DJOSER AUTH ──────────────────────────
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]