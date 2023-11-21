from django.urls import path
from .views import pageLisView, PageDetailView

urlpatterns = [
    path('', pageLisView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
]