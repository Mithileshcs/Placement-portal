from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import SignUpFormStu, Profilerec, ProfileUpdateForm ,JobApplicationForm
from .models import CompanyRec ,Profilenewmain, JobApplication
from .forms import CustomUserChangeForm

# Create your views here.


def home(request):

    companyrec = CompanyRec.objects.all()
    

    # Check if the user has already applied for the job
  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #for authentication of the username and password
        user = authenticate(request,username = username , password = password)

        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged In Successfully!")
            # return render(request,'home.html',{'username':username}) this line is if you want to display the username in that page
            return redirect('home')
        else:
            messages.success(request,"There was an error in Login In , try again...")
            return redirect('home')
    else:
       
       
        return render(request, 'home.html',{'companyrec':companyrec})
    



def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged Out Successfully!")
    return render(request, 'home.html',{})


def register_user(request):
    if request.method == 'POST':
        form = SignUpFormStu(request.POST)
        if form.is_valid():
            form.save()

            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username , password=password)

            login(request,user)
            messages.success(request,"You have successfully Registered! , Welcome")
            return redirect('add_record')
        
    else:
        form = SignUpFormStu()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


@login_required
def company_detail(request, company_id):
    company = get_object_or_404(CompanyRec, id=company_id)
    user_profile = Profilenewmain.objects.get(user=request.user)

    # Check if the user has already applied for the job
    job_already_applied = JobApplication.objects.filter(
        user_profile=user_profile, company=company
    ).exists()

    return render(request, 'company_detail.html', {
        'company': company,
        'job_already_applied': job_already_applied,
    })
    
    
@login_required
def add_record(request):
    form = Profilerec(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Create a new Profilenewrec instance but don't save it yet
            new_record = form.save(commit=False)
            # Set the user field to the current user
            new_record.user = request.user
            # Save the record with the user association
            new_record.save()
            messages.success(request, "Record Added Successfully....")
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})



@login_required
def view_profile(request):
    # Retrieve the user's profile
    profile = get_object_or_404(Profilenewmain, user=request.user)

    return render(request, 'view_profile.html', {'profile': profile})



@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile = Profilenewmain.objects.get(user=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('view_profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile = Profilenewmain.objects.get(user=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})



@login_required
def apply_for_job(request, company_id):
    # Retrieve the logged-in user's profile
    user_profile = Profilenewmain.objects.get(user=request.user)
    # Retrieve the company object
    company = CompanyRec.objects.get(id=company_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            # Create a new job application object
            job_application = form.save(commit=False)
            # Associate it with the logged-in user's profile
            job_application.user_profile = user_profile
            # Associate it with the selected company
            job_application.company = company
            # Save the job application
            job_application.save()
            messages.success(request, " Company Registered successfully.")
            # Redirect the user to a success page or another view
            return redirect('home')
    else:
        form = JobApplicationForm()
    return render(request, 'apply_for_job.html', {'form': form, 'user_profile': user_profile, 'company': company})
