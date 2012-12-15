from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Home.homeForms import ContactForm

__author__ = 'Jacob'

def Index(request):
    return render_to_response("Home/index.html", None , context_instance=RequestContext(request))

def About(request):
    return render_to_response("Home/about.html", None , context_instance=RequestContext(request))

def Contact(request):
    return render_to_response("Home/contact.html", None , context_instance=RequestContext(request))

def SendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('Name', '')
            message = request.POST.get('Message', '')
            email = request.POST.get('Email', '')
            email_body = " Name: %s < %s >\n Message: \n %s " %( name, email, message )
            email = EmailMessage(
                'contact from %s' % name,
                email_body,
                to=['etp@etp.com'],
                from_email='etpnoreply@gmail.com',
            )
            email.send(fail_silently=True)
            return HttpResponseRedirect('/about/')

    return HttpResponseRedirect("/")

def Christmas(request):
    return render_to_response("Home/christmas.html", None , context_instance=RequestContext(request))