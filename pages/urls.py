from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/', PageUpdate.as_view(), name='update'),
], 'pages')