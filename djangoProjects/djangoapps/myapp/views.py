from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<htlm><body bgcolor=cyan><h1><div align='center' >welcome to my first app</div></h1></body></htlm>")


# Create your views here.
