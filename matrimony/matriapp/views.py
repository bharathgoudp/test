from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from matriapp.forms import Step1_Form,Step2_Form,Step3_Form,Step4_Form
from matriapp.models import Step1,Step2,Step3,Step4,Castee,Subcastee,Heightt,MotherTonguee,Weightt,Starr,Raasii,Countryy,Statee,Cityy,Agee,Ageto,Religionn
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def myprofile(request):
    return render(request,'my profile.html')

def myhome(request):
    return render(request,'myhome.html')

def selfprofile(request):
    return render(request,'selfprofile.html') 

def photos(request):
    return render(request,'photos.html')

def profiles(request):
    return render(request,'profiles.html')

def search(request):
    return render(request,'search.html')

def step1(request):
    form=Step1_Form()
    return render(request,'step1.html',{'form':form})    
def step2(request):
    form=Step2_Form()
    return render(request,'step2.html',{'form':form})

def step3(request):
    form=Step3_Form()
    return render(request,'step3.html',{'form':form})  

def step4(request):
    form=Step4_Form()
    return render(request,'step4.html',{'form':form})  

# # form function:

@login_required
def matrisave_1(request):
    if request.method == 'POST':
        form = Step1_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(step2)
    else:
        form = Step1_Form()
        return render(request,'index.html',{'form': form})
@login_required

def matrisave_2(request):
    if request.method == 'POST':
        form = Step2_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(step3)
        else:
            form = Step2_Form()
            return render(request, 'step2.html', {'form': form})    
    
    else:
        form = Step2_Form()
        return render(request, 'index.html', {'form': form})
@login_required
def matrisave_3(request):
    if request.method == 'POST':
        form = Step3_Form(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect(step4)
        else:
            form = Step3_Form()
            return render(request, 'step3.html', {'form': form})    
    else:
        form = Step3_Form()
        return render(request, 'index.html', {'form': form})
@login_required
def matrisave_4(request):
    if request.method == 'POST':
        form = Step4_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(myprofile)
        else:
            form = Step4_Form()
            return render(request, 'step4.html', {'form': form})    
    else:
        form = Step4_Form()
        return render(request, 'index.html', {'form': form})








# def edit(request, id):
#     matri = Matridata.objects.get(id=id)
#     return render(request, "edit.html", {'matri': matri})

# def update(request, id):
#     matri = Matridata.objects.get(id=id):
#     form = MatriForm(request.POST, request.FILES, instance = matri)
#     if form.is_valid():
#         form.save()
#         return redirect(myprofile)
#     else:
#         return render(request, "edit.html", {'matri': matri})

# def delete(request, id):
#     matri = Matridata.objects.get(id=id):
#     matri.delete()
#     return redirect(myprofile)










def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpass']
        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, 'index.html')
            else:

                user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password1)
                Log_User=authenticate(username=email,password=password1)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Registered successfully")
                return redirect(step1)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successfull")
            return redirect(myhome)
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'index.html')
    else:
        return redirect(login)



def logout(request):
    auth_logout(request)
    return redirect('/')    