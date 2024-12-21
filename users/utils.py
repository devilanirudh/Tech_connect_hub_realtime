
from .models import Profile,Skill
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def paginationProfile(request,Profile,results):
    page =request.GET.get('page')
    paginator = Paginator(Profile,results)
    try:
        Profile = paginator.page(page)
    except PageNotAnInteger:
        page =1
        Profile = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        Profile = paginator.page(page)

    leftIndex = (int(page)-4)

    if leftIndex<1:
        leftIndex =1

    rightIndex = (int(page)+5)

    if rightIndex>paginator.num_pages:
        rightIndex= paginator.num_pages+1

    custom_range = range(leftIndex,rightIndex)


    return custom_range,Profile

def searchProfiles(request):

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains =search_query)

    print('search:',search_query)
    profile = Profile.objects.distinct().filter(Q(name__icontains=search_query) | 
                                     Q(short_intro__icontains=search_query)|
                                     Q(skill__in=skills))
    return profile,search_query