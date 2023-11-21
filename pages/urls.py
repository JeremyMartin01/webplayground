from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.pages, name='pages'),
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
=======
from .views import pageLisView, PageDetailView

urlpatterns = [
    path('', pageLisView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
>>>>>>> 7be700f87883979e0e370f0c07dbb6b8052f9dda
]