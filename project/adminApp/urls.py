from django.urls import path
from . import views

# app_name = "adminApp"

urlpatterns = [
    path("asd",views.home,name='home'),
    path("signUp",views.register,name="register"),
    path("login",views.login,name='login'),
    path("createEquip",views.CreateEquipment,name="CreateEquip"),
    path("editPW",views.change_password,name="editPW"),
    path("approveuser",views.approve_users,name='approve'),
    path("deluser",views.delete_users,name="delete"),
    path("viewEquip",views.ViewEquip,name="viewequip"),
    path("report",views.report,name="report")
]
