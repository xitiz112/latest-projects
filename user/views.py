
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm,Training_planForm
from django.contrib.auth.models import User

def index(request):
   
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        Rform = RegisterForm(request.POST)
        if Rform.is_valid():
            user = Rform.save()
            
            return redirect('login')  
    else:
        Rform = RegisterForm()
    return render(request, 'register.html', {'Rform': Rform})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('index')  # Customize the URL for the user dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def Training_cost(request):
    if request.method == 'POST':
        Tform = Training_planForm(request.POST)
        if Tform.is_valid():
            Tform.save()  # Save the member information to the database
            # You can customize the redirect URL as needed (e.g., the login page).
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        Tform = Training_planForm()

    return render(request, 'training_form.html', {'Tform': Tform})


def calculate_total_cost(user_id):
    # Retrieve the member's information from the database
    member = User.objects.get(id=user_id)

    # Define the cost of each training plan
    training_plan_costs = {
        'basic': 1000,
        'intermediate': 2000,
        'advanced': 3000
    }
    training_plan_cost = training_plan_costs.get(member.training_plan, 0)

    additional_services_cost = 0
    if member.sauna:
        additional_services_cost += 500  # Adjust the cost as needed
    if member.swimming:
        additional_services_cost += 800  # Adjust the cost as needed
    if member.private_trainer:
        additional_services_cost += member.private_coaching_hours * 200  # Adjust the cost as needed

    # Calculate the total cost
    total_cost = training_plan_cost + additional_services_cost
    return total_cost

def final_cost(request,user_id):
    # Call the calculate_total_cost function to get the total cost
    total_cost = calculate_total_cost(user_id)

    # Retrieve the member's information from the database
    member = User.objects.get(id=user_id)

    context = {
        'member': member,
        'total_cost': total_cost,
    }

    return render(request,'final_cost.html', context)



