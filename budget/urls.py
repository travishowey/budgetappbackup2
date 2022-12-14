from . import views
from django.urls import path

app_name = 'budget'
urlpatterns = [
    path('', views.index, name="index"),
    path('wallet/', views.wallet, name="wallet"),
    path('spending/', views.spending, name="spending"),
    path('reports/', views.reports, name="reports"),
    path('create_transaction', views.create_transaction, name="create_transaction"),
    path('edit_transaction/<int:id>', views.edit_transaction, name="edit_transaction"),
    path('delete_transaction/<int:id>', views.delete_transaction, name="delete_transaction"),

]