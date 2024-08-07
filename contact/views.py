from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
