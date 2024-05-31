from django.urls import path
from system_management import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.log_out, name="log_out"),
]