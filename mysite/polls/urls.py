from django.urls import path
from django.views.generic import TemplateView
from .import views
urlpatterns = [
    path('index/', views.viewlistloai,name="index"),
    path('list/<int:loai_id>',views.viewlisttintuc,name="list"),
    path('tintuc/<int:tintuc_id>',views.viewtintuc,name="tintuc"),
    path('',views.viewkey,name="key")
]