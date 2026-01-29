from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('financial.urls')),
    path('api/v1/', include('supply.urls')),
    path('api/v1/', include('contabil.urls')),
]
