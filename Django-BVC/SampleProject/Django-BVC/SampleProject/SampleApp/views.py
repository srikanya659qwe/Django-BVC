from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def he(request):
	return HttpResponse("<h1>Hello World!</h1>")

def sam(request):
	return HttpResponse("<h2 style=color:green;background-color:yellow><center>Hai..guys welcome to django online session</center></h2>")


def dyn(request,id):
	return HttpResponse("<h1>My Rollnumber is:{}</h1>".format(id))

def data(request,name):
	return HttpResponse("<h1>My Name is:{}</h1>".format(name))

def task(request,a,b):
	return HttpResponse("<h1>My roll number is:{} and My name is :{}</h1>".format(a,b))

def temp(request):
	return render(request,'SampleApp/temp.html',{})

def table(request):
	return render(request,'SampleApp/table.html',{})

def details(request,name,id):
	return render(request,'SampleApp/details.html',{'n':name,'i':id})

def inline(request):
	return render(request,'SampleApp/inline.html')

def internal(request):
	return render(request,'SampleApp/internal.html')

def external(request):
	if request.method=="POST":
		name=request.POST['uname']
		email=request.POST['em']
		mobile=request.POST['mbl']
		password=request.POST['psw']
		cpassword=request.POST['cpsw']

		return render(request,'SampleApp/data.html',{'n':name,'e':email,'m':mobile,'p':password,'cp':cpassword})

	return render(request,'SampleApp/external.html')

def bootstrap(request):
	return render(request,'SampleApp/boot.html')

def offline(request):
	return render(request,'SampleApp/offline.html')


def insert(request):
	return render(request,'SampleApp/insert.html')