from django.shortcuts import render,redirect
from django .contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CaseForm
from .models import Case
# Create your views here.
def adminloginview(request):
    return render(request,'Cases/adminlogin.html')

def authenticateadmin(request):
    username=request.POST['username']
    password=request.POST['password']

    user = authenticate(username=username,password=password)


    #user_exist:
    if user is not None and user.username=="shubham":
        login(request,user)
        return redirect("adminhomepage")
    #doestn't_exist:
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect("adminloginpage")

def adminhomepage(request):
    if request.method=='POST':

        form=CaseForm(request.POST,request.FILES)
        if form.is_valid():
            c=form.save()
            return render(request,"adminhomepage",{'form':CaseForm(),"pdfs":c.pdf.url})
    else:
        form=CaseForm()
    return render(request,"Cases/adminhomepage.html",{'form':form})


def logoutadmin(request):
    return redirect('adminloginpage')
def caseslist(request):
    form=Case.objects.all()

    return render(request,'Cases/caselist.html',{'form':form})

def homepage(request):
    return render(request,'Cases/homepage.html')

def results(request):
    return render(request,'caselist')