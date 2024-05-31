from django.urls import path
from budget_insight import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('view_all_customers/', views.view_all_customers, name="view_all_customers"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('view_customer/<int:customer_id>/', views.view_customer, name="view_customer"),
]