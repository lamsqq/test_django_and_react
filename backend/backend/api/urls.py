from rest_framework import routers
from core.api.urls import router as post_router
from django.urls import path, include

router = routers.DefaultRouter()
router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]
