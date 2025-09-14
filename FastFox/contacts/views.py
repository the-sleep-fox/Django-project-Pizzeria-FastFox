from django.shortcuts import render

from contacts.models import Workers


# Create your views here.

def get_contacts(request):
    workers = get_workers()
    return render(request, 'contacts/contacts.html', {'workers': workers})

def get_workers():
    workers = Workers.objects.all()
    print(f"WORKERS are here: {workers}")
    return workers