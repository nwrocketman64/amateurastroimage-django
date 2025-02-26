from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index-page"),
    path("contact", views.ContactPage.as_view(), name="contact-page"),
    path("contact-submitted", views.ContactSubmitPage.as_view(), name="contact-submitted"),
    path("images", views.AstroImageList.as_view(), name="astroimages-list"),
    path("image-view/<int:pk>", views.AstroImageDetails.as_view(), name="astroimage-details"),
    path("about", views.AboutPage.as_view(), name="about-page"),
    path("patch-notes", views.PatchNotePage.as_view(), name="patch-notes-page"),
]