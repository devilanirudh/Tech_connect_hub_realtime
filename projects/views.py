from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import boto3


# Create your views here.

from django.http import HttpResponse

from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.db.models import Q
from .utils import searchProjects,paginationProjects


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    # projectobj = None
    # for i in projectsList:
    #     if i['id']==pk:
    #         projectobj = i
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount


        # update project votecount
        messages.success(request,'Your review was successfully submitted')
        return redirect('project',pk=projectObj.id)
    context = {
        "projectobj" :projectObj,
        "tags":tags,
        "form":form
    }

    #     "projectobj":projectobj
    return render(request, "projects/single_projects.html",context)

def projects(request):
   # msg = " hello,you are on the single_projects page"
   # number = 9
    projects,search_query =searchProjects(request)
    custom_range,projects = paginationProjects(request,projects,6)
    
    context = {
       # "msg":msg,
       # "number":number,
        "project_list":projects,
        "search_query":search_query,
        "custom_range":custom_range
    }
    return render(request, "projects/projects.html",context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        boto3.set_stream_logger('botocore', level='DEBUG')

        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST,request.FILES or None)
        #print(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag,created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {
        'form':form
    }
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def updateproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(title=pk)
    form = ProjectForm(instance=project)
    obj = get_object_or_404(Project, title=pk)
    print(project)
    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', " ").split()
        print("Data :", newtags)
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag,created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
        
    context = {'form': form,'project':project}
    return render(request,"projects/project_form.html", context)



@login_required(login_url="login")
def deleteproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(title=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {
        "object":project
    }
    return render(request,"project-delete.html",context)