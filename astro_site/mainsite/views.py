from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.db import models

# Import the needed classes.
from .forms import RequestForm
from .models import AstroImage, Request

# Create your views here.


class IndexPage(TemplateView):
    """
    Index Page: The class delivers a view with the lastest image.
    """
    # Set the template.
    template_name = "mainsite/index.html"


    # Add the title, path, and the latest image.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the earliest project.
        try:
            images = AstroImage.objects.all().order_by("-date_taken")
            lastest_image = images[0]
        except:
            # If failed, return blank.
            lastest_image = []

        # Update and return the context.
        context["title"] = "Home"
        context["path"] = "/home"
        context["image"] = lastest_image
        return context
    

class ContactPage(CreateView):
    """
    Contact Page: Renders the contact page using the request model.
    """
    # Set the template, model, form, and url redirect.
    template_name = "mainsite/contact.html"
    model = Request
    form_class = RequestForm
    success_url = "/contact-submitted"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        context["path"] = "/contact"
        return context
    

class ContactSubmitPage(TemplateView):
    """
    Contact Submit Page: Renders the contact success submit page.
    """
    # Set the template.
    template_name = "mainsite/contact-submit.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message Received"
        context["path"] = "/contact"
        return context
    

class AstroImageList(ListView):
    """
    Astro Image List: Renders a list of images.
    """
    template_name = "mainsite/images-list.html"
    model = AstroImage
    ordering = ["-date_taken"]
    context_object_name = "images"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            queryset = queryset.filter(
                models.Q(object__icontains=search_query) |
                models.Q(location__icontains=search_query) |
                models.Q(telescope__icontains=search_query) |
                models.Q(comment__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Full List of Images"
        context["path"] = "/images"
        context["search_query"] = self.request.GET.get('q', '')
        return context
    

class AstroImageDetails(DetailView):
    """
    Astro Image Details: Renders a single image.
    """
    template_name = "mainsite/image-view.html"
    model = AstroImage
    context_object_name = "image"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "View of"
        context["path"] = "/images"
        return context
    

class AboutPage(TemplateView):
    """
    About Page: Renders the about page.
    """
    # Set the template.
    template_name = "mainsite/about.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["path"] = "/about"
        return context


class PatchNotePage(TemplateView):
    """
    Patch Note Page: Renders the patch note page.
    """
    # Set the template.
    template_name = "mainsite/patch-notes.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Patch Notes"
        context["path"] = "/about"
        return context
