from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from projectapp.models import *

def index3(Request):
	return render(Request,'index3.html')

def success(Request):
	return render(Request,'success.html')
 
def registerView(Request):
	name=Request.GET.get("name")
	email=Request.GET.get("email")
	password=Request.GET.get("password")
	cpassword=Request.GET.get("cpassword")
	p=Register(name=name,email=email,password=password,cpassword=cpassword)
	p.save()
	return render(Request,'index3.html')

def loginView(Request):
	flag=False
	name=Request.GET.get("name")
	password=Request.GET.get("password")
	user=Register.objects.all()
	for i in user:
		if(i.name==name and i.password==password):
			flag=True
			#allData=Register.objects.all()
			return render(Request,'success.html')

	if(flag==False):
		return render(Request,'unsuccess.html')

#------------------------------------------------------------
#File Upload

def upload(Request):
    if Request.method == 'POST' and Request.FILES['myfile']:
        uploaded_file = Request.FILES['myfile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(name)
        return render(Request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(Request, 'upload.html')
    
def uploadview(Request):
	return render(Request,'index3.html')

#----------------------------------------------------------------

def unsuccess(Request):
	return render(Request,'index3.html')
