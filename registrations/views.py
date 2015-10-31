from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registrations.models import UserProfiles
from registrations.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from gwalior.models import Complaints


# def index(request):
# 	if not request.user.is_authenticated():
# 		return render(request, 'base.html', {})
# 	else:
# 		info = request.user.userprofiles
# 		context = {'info':info}
# 		return render_to_response('base.html', context, context_instance=RequestContext(request))


def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password=form.cleaned_data['password'])
			user.save()

			registration = UserProfiles(user=user, first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'],
				address = form.cleaned_data['address'],area = form.cleaned_data['area'],pin = form.cleaned_data['pin'],telephone = form.cleaned_data['telephone'],
				mobile = form.cleaned_data['mobile'], education = form.cleaned_data['education']
				)
			if 'picture' in request.FILES:
				registration.picture = request.FILES['picture']

			registration.save()
			return HttpResponseRedirect('/profile')

		else:
			return render_to_response('registrations/register.html',{'form':form, 're':"active"}, context_instance=RequestContext(request))


	else:
	 	form = RegistrationForm()
	   	context = {'form': form, 're':"active"}
	  	return render_to_response('registrations/register.html', context, context_instance=RequestContext(request))

@login_required
def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('registrations/login/')
	comp = Complaints.objects.all().filter(username=request.user.username)
	info = request.user.userprofiles
	context = {'info':info, 'pr':"active", 'comp':comp}
	return render_to_response('registrations/profile.html', context, context_instance=RequestContext(request))



def loginrequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			signin = authenticate(username=username, password=password)
			if signin is not None:
				login(request, signin)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('registrations/login.html', {'form':form, 'ln':"active"}, context_instance=RequestContext(request))
		else:
			return render_to_response('registrations/login.html', {'form':form, 'ln':"active"}, context_instance=RequestContext(request))

		
	else:
		form = LoginForm()
		context = {'form': form, 'ln':"active"}
		return render_to_response('registrations/login.html', context, context_instance=RequestContext(request))


def logoutrequest(request):
	logout(request)
	return HttpResponseRedirect('/')