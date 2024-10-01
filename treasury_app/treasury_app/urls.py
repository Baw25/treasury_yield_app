from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/treasury-yields/', include('treasury.urls')),
    path('api/orders/', include('order.urls')),
]

