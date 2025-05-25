from django.shortcuts import render

# Create your views here.

def get_contacts(request):
    return render(request, 'contacts/contacts.html')
