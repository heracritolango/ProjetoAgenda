from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(requests):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(
        requests,
        'contact/index.html',
        context,
    )