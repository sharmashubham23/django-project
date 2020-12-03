from django.shortcuts import render, HttpResponse
from .models import Customer
# from .forms import CustomerForm

def index(request):
	
	return render(request, 'index.html')

def data(request):
    if request.method == "POST":
        # GET POST PARAMETERS
        X_axis_Data = request.POST['X_axis_Data']
        Y_axis_Data = request.POST['Y_axis_Data']

        x_data = X_axis_Data.split(',')
        y_data = Y_axis_Data.split(',')
        print(x_data)
        post = Customer()
        post.X_axis_Data = request.POST.get('X_axis_Data')
        post.Y_axis_Data = request.POST.get('Y_axis_Data')
        post.save()
  
        context = {'xaxis': x_data, 'yaxis': y_data}
        print(context)
        return render(request, 'view.html', context)

    else:
        return HttpResponse("404 - Page Not Found")

