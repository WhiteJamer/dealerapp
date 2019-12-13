from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include
from dealers.api.urls import router as dealer_router
from dealership.api.urls import router as dealership_router
from cars.api.urls import router as car_router

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('customauth.urls')),
    path('dealers/', include('dealers.urls')),
    path('dealerships/', include('dealership.urls')),
    path('cars/', include('cars.urls')),
    path('users/', include('uprofile.urls')),
    # API
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(dealer_router.urls)),
    path('api/', include(dealership_router.urls)),
    path('api/', include(car_router.urls))
]
