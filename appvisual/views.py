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
        # check for error inputs
        # username should be under 10 characters
        # if len(username) > 10:
        #     messages.error(request, "Username must be under 10 characters")
        #     return redirect('/shop')
        # if not username.isalnum():
        #     messages.error(
        #         request, "Username must contains characters and numbers only.")
        #     return redirect('/shop')
        # if pass1 != pass2:
        #     messages.error(request, "Password does not match")
        #     return redirect('/shop')

        # #  Creat the user
        # myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.save()
        # messages.success(
        #     request, "Your Account is Successfully created. Please Sign Up using credentials.")
        # return redirect('/shop')
        context = {'xaxis': x_data, 'yaxis': y_data}
        print(context)
        return render(request, 'view.html', context)

    else:
        return HttpResponse("404 - Page Not Found")


# def handelLogin(request):
#     if request.method == 'POST':
#         loginusername = request.POST['loginusername']
#         loginpass = request.POST['loginpass']

#         user = authenticate(username=loginusername, password=loginpass)

#         if user is not None:
#             # A backend authenticated the credentials
#             login(request, user)
#             messages.success(request, "Successfuly Logged In")
#             return redirect('/shop/')
#         else:
#             # No backend authenticated the credentials
#             messages.error(request, "Invalid Credentials, please try again")
#             return redirect('/shop/')

#     return HttpResponse("404 - Page Not Found")