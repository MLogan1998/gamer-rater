from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from raterapi.views import register_user, login_user, Games, Categories, ReviewsViewSet, ImageViewSet, RatingVIewSet
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', Games, 'game')
router.register(r'categories', Categories, 'category')
router.register(r'reviews', ReviewsViewSet, 'review')
router.register(r'image', ImageViewSet, 'image')
router.register(r'rating', RatingVIewSet, 'rating')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('raterreports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
