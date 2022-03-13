from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# registration function

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # for validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created! You Can Login Now {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()   # This is an instance from the user creation form modul
    return render(request, 'users/register.html', {'form': form}) # Function render takes 'request parameter' this is required parameter, then the template that will render it, then we want a variable {'form'} that we want to assgn to it the instance form that we created 'form = userCreationForm'.



# Adding some restriction to make the user must login
@login_required
def profile(request):
    # creating instances from the forms
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { 'u_form' : u_form, 
                'p_form' : p_form }

    return render(request, 'users/profile.html', context)

