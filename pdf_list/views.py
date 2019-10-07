from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import PDFDocument

class HomePageView(TemplateView):

        template_name = "home.html"

class PDFlistView(ListView):
    model = PDFDocument
