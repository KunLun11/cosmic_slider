from django.shortcuts import render
from slider.models.sliders import Slider


def home(request):
    slides = Slider.objects.filter(is_active=True).order_by("order")
    return render(request, "slider/home.html", {"slides": slides})


