from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewset
from book import views

router = DefaultRouter()
router.register('book',BookViewset,basename='book')

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]