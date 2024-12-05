from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactUsForm
from about.models import Contact

# Contact us view
def contact_us_view(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Successfully submitted...")
            return redirect('contact_us')
    else:
        form = ContactUsForm()
    form = ContactUsForm()
    contact_info = Contact.objects.all()

    context = {
        'form': form,
        'contact_info': contact_info
    }

    return render(request, 'contact_us.html', context)


