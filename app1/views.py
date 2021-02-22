from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from app1.models import tbl_user
from app1.models import tbl_idgen
from django.http import HttpResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage



# Create your views here.

    
def index(request):
    return render(request,'index.html')

def viewtree(request):
    try:
        rootUser = tbl_user.objects.get(userId = 1)
    except tbl_user.DoesNotExist:
        rootUser = None
    users = tbl_user.objects.filter(~Q(userId = 1))
    return render(request,'viewtree.html',{'ruser':rootUser,'user':users})

def userRegForm(request):
    allUsers = tbl_user.objects.all()
    return render(request,'userRegForm.html',{'users':allUsers})

def userReg(request):
    if request.method == "POST":
        userImage = request.FILES['uploadImage']
        fs = FileSystemStorage()
        filename = fs.save(userImage.name, userImage)
        uploaded_file_url = fs.url(filename)
        data1 = tbl_idgen.objects.get(id=1)
        data = tbl_user()
        data.name = request.POST.get('userName')
        data.email = request.POST.get('userEmail')
        data.password = request.POST.get('userPass')
        data.title = request.POST.get('userTitle')
        data.userImage = uploaded_file_url
        data.currentPoints = 0
        parentValue = int(request.POST.get('parent'))
        data1.user += 1
        data.userId = data1.user
        if (parentValue == 0):
            data.parentNodeId = 0
            data.save()
            data1.save()
        else:
            data.parentNodeId = request.POST.get('parent')
            data2 = tbl_user.objects.get(userId = data.parentNodeId)
            data2.currentPoints += 1
            data2.save()
            if data2.parentNodeId > 0:
                cpoints = 1
                parid = data2.parentNodeId
                while(parid > 0):
                    data3 = tbl_user.objects.get(userId = parid)
                    cpoints = cpoints/2
                    data3.currentPoints += cpoints
                    data3.save()
                    parid = data3.parentNodeId
            data.save()
            data1.save()
        return redirect('/')
    else:
        return HttpResponse("error")



