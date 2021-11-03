from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api.urls import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

