#from django.http import *
#from django.shortcuts import render_to_response,redirect
#from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
#from django.conf import settings
 
def isLoggedIn(request):
    user = request.user
    if not user.is_authenticated():
        loggedIn = [0,[]]
    else:
        loggedIn = 1
        userGroups = user.groups.values_list('name',flat=True)

        loggedIn = [loggedIn, userGroups]
 
    return loggedIn
 
