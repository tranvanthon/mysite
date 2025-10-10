from django.shortcuts import render

# Create your views here.
def profile(request):
    # Logic to display user profile
    return render(request, 'accounts/profile.html')

def edit_profile(request):
    # Logic to edit user profile
    return render(request, 'accounts/edit_profile.html')    

def edit_avatar(request):
    # Logic to edit user avatar
    return render(request, 'accounts/edit_avatar.html')