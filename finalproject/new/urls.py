from django.urls import path
from . import views
app_name = 'new'

urlpatterns = [path("", views.index, name = "index"),
               path("img_upload", views.upload, name = "img_upload"),
              ]