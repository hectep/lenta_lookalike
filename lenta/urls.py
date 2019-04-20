from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from lenta import views


router = routers.DefaultRouter()
urlpatterns = [
    path('lenta/', views.NewsList.as_view()),
    path('post/<str:pk>/', views.NewsPostDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += staticfiles_urlpatterns()
