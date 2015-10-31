from django.shortcuts import render
from django.http import HttpResponse
from gwalior.forms import ComplaintsForm, StatusForm
#from gwalior.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
#from gwalior.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gwalior.models import Complaints




def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # for instance in UserProfile.objects.all():
    #     print(instance.first_name)


    # if request.user.is_anonymous():
    #     instance='Guest'
    # else:
    #     instance = UserProfile.objects.get(user=request.user)



    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    

    return render(request, 'gwalior/index.html', {'ho':"active"})



def about(request):
	au="active"
	return render(request, 'gwalior/about.html', {'au':au})

def contact(request):
	return render(request, 'gwalior/contact.html', {'co':"active"})

def add_complaint(request):
	if request.user.is_authenticated():
		info = request.user.userprofiles
		user = request.user
		if request.method == 'POST':
			form = ComplaintsForm(request.POST) 
			if form.is_valid():
				forid = form.save(commit=True)
				valueid = forid.id
				
				# After submission of complaint user will be shown homepage
				return render(request, 'gwalior/after_complaint.html', {'valueid':valueid, 'ac':"active"})
			else:
				print form.errors
		else:
			# If the request was not a POST, display the form to enter details.
			form = ComplaintsForm()

		return render(request, 'gwalior/add_complaint.html', {'form': form, 'info':info, 'user':user, 'ac':"active"})


	else:
		if request.method == 'POST':
			form = ComplaintsForm(request.POST) 
			if form.is_valid():
				forid = form.save(commit=True)
				valueid = forid.id
				# After submission of complaint user will be shown homepage
				return render(request, 'gwalior/after_complaint.html', {'valueid':valueid, 'ac':"active"})
			else:
				print form.errors
		else:
			# If the request was not a POST, display the form to enter details.
			form = ComplaintsForm()

		return render(request, 'gwalior/add_complaint.html', {'form': form, 'info':'nothing', 'user':'nothing', 'ac':"active"})


def complaint_status(request):
	if request.method == 'POST':
			form = StatusForm(request.POST) 
			if form.is_valid():
				cd = form.cleaned_data['idnumber']
				#idnumber  = cd.get('idnumber')
				status = Complaints.objects.get(pk=cd)
				form = StatusForm()
				# After submission of complaint user will be shown homepage
				return render(request, 'gwalior/complaint_status.html', {'form':form, 'status':status, 'cs':"active"})
			
	else:
			# If the request was not a POST, display the form to enter details.
		form = StatusForm()

	return render(request, 'gwalior/complaint_status.html', {'form':form, 'cs':"active"})



# def register(request):

#     # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
#     registered = False

#     # If it's a HTTP POST, we're interested in processing form data.
#     if request.method == 'POST':
#         # Attempt to grab information from the raw form information.
#         # Note that we make use of both UserForm and UserProfileForm.
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)

#         # If the two forms are valid...
#         if user_form.is_valid() and profile_form.is_valid():
#             # Save the user's form data to the database.
#             user = user_form.save()

#             # Now we hash the password with the set_password method.
#             # Once hashed, we can update the user object.
#             user.set_password(user.password)
#             user.save()

#             # Now sort out the UserProfile instance.
#             # Since we need to set the user attribute ourselves, we set commit=False.
#             # This delays saving the model until we're ready to avoid integrity problems.
#             profile = profile_form.save(commit=False)
#             profile.user = user

#             # Did the user provide a profile picture?
#             # If so, we need to get it from the input form and put it in the UserProfile model.
            
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']

#             # Now we save the UserProfile model instance.
#             profile.save()

#             # Update our variable to tell the template registration was successful.
#             registered = True

#         # Invalid form or forms - mistakes or something else?
#         # Print problems to the terminal.
#         # They'll also be shown to the user.
#         else:
#             print user_form.errors, profile_form.errors

#     # Not a HTTP POST, so we render our form using two ModelForm instances.
#     # These forms will be blank, ready for user input.
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     # Render the template depending on the context.
#     return render(request,
#             'gwalior/register.html',
#             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



# def user_login(request):

#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
#                 # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
#                 # because the request.POST.get('<variable>') returns None, if the value does not exist,
#                 # while the request.POST['<variable>'] will raise key error exception
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Use Django's machinery to attempt to see if the username/password
#         # combination is valid - a User object is returned if it is.
#         user = authenticate(username=username, password=password)
        
#         # If we have a User object, the details are correct.
#         # If None (Python's way of representing the absence of a value), no user
#         # with matching credentials was found.
#         if user:
#             # Is the account active? It could have been disabled.
#             if user.is_active:
#                 # If the account is valid and active, we can log the user in.
#                 # We'll send the user back to the homepage.
#                 login(request, user)
#                 return HttpResponseRedirect('/gwalior/')
#             else:
#                 # An inactive account was used - no logging in!
#                 return HttpResponse("Your gwalior account is disabled.")
#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")

#     # The request is not a HTTP POST, so display the login form.
#     # This scenario would most likely be a HTTP GET.
#     else:
#         # No context variables to pass to the template system, hence the
#         # blank dictionary object...
#         return render(request, 'gwalior/login.html', {})


# @login_required
# def restricted(request):
#     return HttpResponse("Since you're logged in, you can see this text!")

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/gwalior/')
