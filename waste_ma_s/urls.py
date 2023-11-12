from django.urls import path
from waste_ma_s import views
# from waste_ma_s.views import index

app_name = "waste_ma_s"

urlpatterns = [
    path('', views.index),
]
