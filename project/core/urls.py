from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("",views.home,name='home'),
    path("signUp",views.register,name="register"),
    path("Userlogin",views.login,name='Userlogin'),
    path("createEquip",views.CreateEquipment,name="equipment"),
    path("editPW",views.change_password,name="editPW"),
    path('book', views.reserve_equipment, name='book'),
    path("history",views.reservationHistory,name='history'),
    path("logout",views.logout_view,name='logout')
]
