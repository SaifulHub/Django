from django.contrib import admin
from django.urls import path,include  # have to add 'include' to add other apps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',include('employee.urls')),
    path('login/',include('employee.urls'))
]
