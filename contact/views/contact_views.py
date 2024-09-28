from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(requests):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]

    context = {
        'contacts': contacts,
    }

    return render(
        requests,
        'contact/index.html',
        context,
    )

def contact(requests, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': single_contact,
    }

    return render(
        requests,
        'contact/contact.html',
        context,
    )    