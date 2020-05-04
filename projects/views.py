from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project
# Create your views here.
def project_list(request):
    return render(request, 'projects/index.html')
def all_projects(request):
    #query table
    p=Project.objects.all()
    print(p)
    return  render(request,'projects/all_projects.html',{'projects':p})
def project_detail(request,pk):
    project=Project.objects.get(pk=pk)
    return render(request,'projects/project_detail.html',{'project':project})