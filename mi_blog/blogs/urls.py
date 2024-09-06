from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='pages'),
    path('<int:page_id>/', views.page_detail, name='page_detail'),
]
