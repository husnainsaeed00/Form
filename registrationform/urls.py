from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registrationform.urls')),  # Include your app's URL patterns here
    # Add other URL patterns for your project as needed
]
