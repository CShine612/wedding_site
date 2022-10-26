from email.policy import default
from logging import PlaceHolder
from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Fieldset, Field, Div
from crispy_forms.bootstrap import StrictButton, PrependedText, PrependedAppendedText
from django.utils.safestring import mark_safe
from django.utils.dateparse import parse_datetime
from django.templatetags.static import static


from .models import Guest, PlusOneGuest


class GuestSearch(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("rsvp_start")
        self.helper.form_class = "guest-search-form form-control"
        self.helper.layout = Layout(Div(Field("first_name", placeholder="First Name", css_class="first-name-field"), 
                                        Field("surname", placeholder="Surname", css_class="surname-field"),
                                        StrictButton(f'<img src="{static("images/search.png")}" class="guest-search-img" alt="search">', type="submit", css_class="guest-search-button", id="save"),
                                        css_class="guest-search-bar"
                                    ))
        self.helper.form_show_labels = False

    first_name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "guest-form"
        if self.instance.plus_one:
            self.helper.layout = Layout(
                Fieldset(
                    f"{self.instance.first_name} {self.instance.surname}",
                    Fieldset("Basic", "attending", css_class="basic"),
                    Fieldset("info", "email", "meal", css_class="info"),
                    Field("comments"),
                    Field("plus_one_attendance"),
                    )
            )
        else:
            self.helper.layout = Layout(
                Fieldset(
                    f"{self.instance.first_name} {self.instance.surname}",
                    Fieldset("Basic", "attending", css_class="basic"),
                    Fieldset("info", "email", "meal", css_class="info"),
                    Field("comments"),
                    )
            )

    MEAL_CHOICES = (
        ("Meat", "Meat"),
        ("Fish", "Fish"),
        ("Vegan", "Vegan"),
        ("None", "None"),
    )
    ATTENDING_CHOICES = (
        (True, "Yes"),
        (False, "No")
    )
    first_name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    attending = forms.ChoiceField(choices=ATTENDING_CHOICES,
                                  widget=forms.RadioSelect())
    email = forms.EmailField(required=False)
    meal = forms.ChoiceField(choices=MEAL_CHOICES,
                             widget=forms.RadioSelect(),
                             required=False)
    comments = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    plus_one = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    plus_one_attendance = forms.ChoiceField(choices=ATTENDING_CHOICES, widget=forms.RadioSelect(), required=False)
    group = forms.BooleanField(widget=forms.HiddenInput(), required=False)


class PlusOneForm(GuestForm):
    class Meta:
        model = PlusOneGuest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        if "instance" in kwargs.keys():
            invited_guest = kwargs["instance"].invited_guest
        else:
            invited_guest = kwargs.pop("invited_guest")
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "plus-one-form"
        self.helper.layout = Layout(
            Fieldset(
                f"{invited_guest.first_name} {invited_guest.surname} Plus One",
                Fieldset("Basic", "first_name", "surname", css_class="basic"),
                Fieldset("info", "email", "meal", css_class="info-plus-one"),
                Field("comments"), 
                )
        )
        self.attending = True


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("send_contact")
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(Div(Field("first_name", placeholder="First Name"), 
                                        Field("last_name", placeholder="Surname"),
                                        Field("email_address", placeholder="Email"),
                                        Field("message", placeholder="Please enter your message here"),
                                        css_class="contact-form"
                                    ))
        self.helper.form_show_labels = False

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class AccomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(Field(PrependedText("location",  mark_safe(f"<img class='in-bar-image fixed-field' src='{static('images/location.png')}'>"), css_class="location-search fixed-field"), css_class="fixed-field"),
                                    Div(Field(PrependedText("check_in", mark_safe(f"<img class='in-bar-image' src='{static('images/calendar.png')}'>")), type="date"), 
                                        Field(PrependedText("check_out", mark_safe(f"<img class='in-bar-image' src='{static('images/next.png')}'>")), type="date"), 
                                        css_class="accom-search-dates"),
                                    Div(Field(PrependedAppendedText("adults", mark_safe(f"<img class='in-bar-image' src='{static('images/user.png')}'>"), "Adults")), 
                                        Field(PrependedAppendedText("children", mark_safe(f"<img class='in-bar-image child' src='{static('images/user.png')}'>"), "Children")), 
                                        css_class="accom-search-guests"))
        self.helper.form_show_labels = False
        self.helper.form_class = "accom-form-obj"

    default_checkin_date = parse_datetime('2023-11-11T12:00:00')
    default_checkout_date = parse_datetime('2023-11-13T12:00:00')

    location = forms.CharField(max_length=50, initial="Doolin, Co.Clare, Ireland", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    check_in = forms.DateField(initial=default_checkin_date, widget=forms.SelectDateWidget())
    check_out = forms.DateField(initial=default_checkout_date, widget=forms.SelectDateWidget())
    adults = forms.IntegerField(initial=1)
    children = forms.IntegerField(initial=0)
