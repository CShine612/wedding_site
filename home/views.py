from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import GuestForm, ContactForm, GuestSearch, PlusOneForm, AccomForm
from .models import FAQ, Guest, PlusOneGuest

# Create your views here.


def home(request):
    return render(request, "home/index.html")


def venue(request):
    return render(request, "home/venue.html")


def rsvp_start(request):
    form = GuestSearch()
    context = {
        "form": form,
        "search_result": None
    }
    if request.method == "POST":
        form = GuestSearch(request.POST)
        if form.is_valid():
            exact_match = Guest.objects.filter(first_name__iexact=form.cleaned_data["first_name"]).filter(surname__iexact=form.cleaned_data["surname"])
            context = {
                "form": form,
                "search_results": exact_match,
            }
        return render(request, "home/rsvp_start.html", context)
    else:
        return render(request, "home/rsvp_start.html", context)


def rsvp(request, id):
    main_guest = Guest.objects.get(id=id)
    if main_guest.group > 0:
        guest_group = list(Guest.objects.filter(group=main_guest.group))
        guest_group.remove(main_guest)
    else:
        guest_group = []
    form_set = [GuestForm(instance=main_guest)]
    if main_guest.plus_one:
        if hasattr(main_guest, "plus_one_guest"):
            form_set.append(PlusOneForm(instance=main_guest.plus_one_guest))
        else:
            form_set.append(PlusOneForm(invited_guest=main_guest))
    if len(guest_group) > 0:
        for guest in guest_group:
            form_set.append(GuestForm(instance=guest))
            if guest.plus_one:
                if hasattr(guest, "plus_one_guest"):
                    form_set.append(PlusOneForm(instance=guest.plus_one_guest))
                else:
                    form_set.append(PlusOneForm(invited_guest=guest))
    context = {
        "form_set": form_set,
    }

    return render(request, "home/rsvp.html", context)


def log_rsvp(request):
    form_set = request.POST
    group_number = form_set[0].group
    for form in form_set:
        form.group = group_number
        if form.is_valid():
            form.save()
    return redirect("rsvp_success")


def rsvp_success(request):
    return render(request, "home/rsvp_success.html")


def accommodation(request):
    form = AccomForm()
    context = {
        "form": form,
    }
    return render(request, "home/accommodation.html", context)


def ceremony(request):
    return render(request, "home/ceremony.html")


def day_2(request):
    return render(request, "home/day_2.html")


def faq(request):
    context = {
        "faqs": FAQ.objects.all(),
    }
    return render(request, "home/faq.html", context)


def gifts(request):
    return render(request, "home/gifts.html")


def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, "home/contact.html", context)


def send_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contact_success")


def contact_success(request):
    return render(request, "home/contact_success.html")
