from django.urls import path
from django.views.generic import TemplateView
from .import views
urlpatterns = [
    path('', views.viewlistloai,name="index"),
    path('list/<int:loai_id>',views.viewlisttintuc,name="list")
]