
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            # For example, you can create a new Registration object and save it
            registration = form.save()
            # Redirect to a success page or another URL
            return redirect('success_page')
    else:
        form = RegistrationForm()
    
    return render(request, 'registrationform/registration_form.html', {'form': form})
