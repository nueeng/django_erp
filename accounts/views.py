from django.shortcuts import render

# Create your views here.

def sign_in_view(request):
    return render(request, 'accounts/sign_in.html')
