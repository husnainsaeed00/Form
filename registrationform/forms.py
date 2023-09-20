from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Enter Your First Name')
    last_name = forms.CharField(max_length=100, label='Enter Your Last Name')
    email = forms.EmailField(label='Enter Your Email')
    new_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput,
        label='Create a New Password',
        help_text='Password must be at least 8 characters long and contain only lowercase letters and digits.'
    )
    
    ACCOUNT_CHOICES = [
        ('personal', 'Personal Account'),
        ('business', 'Business Account'),
    ]
    account_type = forms.ChoiceField(
        choices=ACCOUNT_CHOICES,
        widget=forms.RadioSelect,
        label='Account Type'
    )
    
    terms_and_conditions = forms.BooleanField(
        required=True,
        label='I accept the terms and conditions'
    )
    
    # Add more form fields as needed, such as profile picture, age, referrer, bio, etc.
