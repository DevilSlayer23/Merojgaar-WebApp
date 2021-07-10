from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def contact(request):

    if request.method == "POST":
        contact = ContactForm(request.POST)
        print(contact)
        if contact.is_valid():
            contact.save()
            
            return render(request,'contact/contact.html')

    return render(request, 'contact/contact.html')