from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm,EquipmentForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import Equipment,Reservation
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='Userlogin')
def home(request):
    return render(request,"user/home.html")

def CreateEquipment(request):
    form = EquipmentForm()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equip = form.save(commit=False)
            equip.assigned_to = request.user
            equip.save()
            return redirect("home")
    context = {"eForm":form}
    return render(request,"user/bookEquip.html",context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,email=email,password=password,username=username)
            print(user)
            if user is not None:
                auth.login(request,user)
            return redirect("home")
    context = {'logF':form}
    return render(request,"user/login.html",context)   

def logout_view(request):
    logout(request)
    return HttpResponse("logout") 

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect("Userlogin")
    context = {"regForm":form}
    return render(request,"user/signUp.html",context=context)

@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'user/change_password.html', context)

@login_required(login_url='login')
def reservationHistory(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request,"user/reserveHistory.html",{"reservations":reservations})


@login_required(login_url='login')
def reserve_equipment(request):
    if request.method == "POST":
        selected_equipment = request.POST.get("selected_equipment")
        equipment = Equipment.objects.get(pk=selected_equipment)
        start_date = request.POST.get('reserved_from')
        end_date = request.POST.get("reserved_to")
        reservation = Reservation(
            user = request.user,
            equipmentId = equipment,
            reserved_from = start_date,
            reserved_to = end_date,
        )
        reservation.save()
        return render(request,"user/reserveEquipment.html")
    equipments = Equipment.objects.all()
    reserved_equipments = equipments.exclude(reservation__isnull=False)
    context = {"equipments":reserved_equipments}
    return render(request, 'user/reserveEquipment.html', context)
