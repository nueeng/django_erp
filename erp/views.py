from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/inventory')
    else:
        return redirect('/sign-in')
    
def erp_home(request):
    if request.method == 'GET':
        return render(request, 'erp/inventory.html')