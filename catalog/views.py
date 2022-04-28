from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
from .models import student


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_students = student.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_students': num_students,
    }
    model=student
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
    
from django.views import generic
from django.http import HttpResponse
import os

class StudentListView(generic.ListView):
    model = student
    
def introduction_page(request):
    return render(request,"catalog/introduction_page.html",locals())
    
def counting_principle(request):
    return render(request, 'catalog/counting_principle.html', locals())
    
def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        #passwd = request.POST.get("password")
        #print("student.objects.get(std_No==username):", student.objects.filter(std_No=username, passwd=passwd))
        print("student.objects.get(std_No==username):", student.objects.filter(std_No=username))
        try:
            username = username.upper()
            student.objects.get(std_No=username)
            students = student.objects.get(std_No=username)
            request.session['is_login'] = True
            request.session['username'] = username
            request.session['name'] = students.name
            return render(request, "catalog/personal_page.html", locals())
        except:
            error_msg = "無此代號"
            return render(request, 'catalog/login.html', {'login_error_msg':error_msg})
    else:
        if(request.session.get('is_login')):
            return render(request, 'catalog/personal_page.html', locals())
    return render(request, 'catalog/login.html', locals())
    
    
def logout(request):
    request.session.delete()
    return redirect('/catalog/login/')
    
def personal_page(request):
    if(request.session.get('is_login')):
        username = request.session.get('username')
        students = student.objects.get(std_No=username)
        return render(request, 'catalog/personal_page.html', locals())
    return HttpResponse("尚未登入!")
    #return HttpResponseRedirect('catalog/personal_page.html')


from catalog.tasks import task_count
from django.urls import reverse
    
def uploadFile(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None)
        if not myFile:  
            return HttpResponse("no files for upload!")  
        username = request.session.get('username')
        path='Video/'+username
        if not (os.path.exists(path)):
            os.mkdir(path)
        destination = open(os.path.join(path, myFile.name),'wb+')
        for chunk in myFile.chunks(): 
            destination.write(chunk)  
        destination.close()
        score = task_count.apply_async((username, myFile.name))
        
        return render(request, 'catalog/success_upload.html')



