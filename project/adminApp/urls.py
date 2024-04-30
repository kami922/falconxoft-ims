from django.urls import path
from . import views

# app_name = "adminApp"

urlpatterns = [
    path("",views.home,name='home2'),
    path("signUp",views.register,name="register"),
    path("adlogin",views.login_view,name='adlogin'),
    path("createEquip",views.CreateEquipment,name="CreateEquip"),
    path("editPW",views.change_password,name="editPW"),
    path("approveuser",views.approve_users,name='approve'),
    path("deluser",views.delete_users,name="delete"),
    path("viewEquip",views.ViewEquip,name="viewequip"),
    path("report",views.report,name="report"),
    path("cancelReservation",views.cancelReservation,name="cancelReservation"),
    path("logout",views.logout_view,name="logout")
    # path("bookEquip",views.createEquip,name="bookEquip")
]

print(urlpatterns)