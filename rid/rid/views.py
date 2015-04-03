# importing django render shortcut
from django.shortcuts import render

# importing login required decorator
from django.contrib.auth.decorators import login_required as auth

@auth
def HomePageView(request):
        return render(request, "home.html")
