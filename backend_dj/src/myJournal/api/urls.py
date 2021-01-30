from django.urls import path

from .views import bulletJListView, bulletJDetailtView

urlpatterns = [
    path('',bulletJListView.as_view()),
    path('<pk>', bulletJDetailtView.as_view()),
]
