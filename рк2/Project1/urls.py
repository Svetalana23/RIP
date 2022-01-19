from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from stocks import views as views

router = routers.DefaultRouter()
router.register('lang', views.LangViewSet)
router.register('env', views.EnvViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('report/', views.report),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
