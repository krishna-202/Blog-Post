from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
    'author':'Valmiki',
    'title':'Ramayana',
    'content':'Ramayana content',
    'date_posted':'December 12, 2020'
    },

    {
    'author':'Vedavyasa',
    'title':'Mahabharata',
    'content':'Mahabharata content',
    'date_posted':'December 12, 2020'
    }
]

context={'posts':posts}
def home(request):
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
# Create your views here.
