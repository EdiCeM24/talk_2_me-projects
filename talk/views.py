from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse # this is corresponding with the one on comment below.
from .models import Talk
#from . import forms

# Create your views here.
def index(request):
    talks = Talk.objects.all()
    return render(request, "index.html", {'talks': talks}) # return HttpResponse('<h1>Hello, World!</h1>')


"""def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            render(request, "make_payment.html", {"payment": payment})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form': payment_form})"""
         