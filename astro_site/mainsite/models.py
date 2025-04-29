from datetime import datetime
from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from PIL import Image, ImageDraw, ImageFont
from pytz import timezone

# Create your models here.


class AstroImage(models.Model):
    """
    Astro Image: A model for how each image is saved.
    """
    object = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    image_standard = ImageSpecField(source='image',
                                    processors=[ResizeToFill(800, 450)],
                                    format='JPEG',
                                    options={'quality': 80})
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(300, 200)],
                                 format='JPEG',
                                 options={'quality': 60})
    location = models.CharField(max_length=255)
    telescope = models.CharField(max_length=255)
    comment = models.TextField()
    date_taken = models.DateTimeField()


    # The method defines how each request appears in the admin section.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.date_taken.astimezone(current_zone)
        
        # Return the correct string.
        return f"{self.object} taken on {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"
    
    # The method controls how images are saved and add watermarks.
    def save(self, *args, **kwargs):
        # Save image before adding the watermark.
        super().save(*args, **kwargs)

        # Open the image.
        photo = Image.open(self.image.path)
        draw = ImageDraw.Draw(photo)

        # Prepare font and get image size.
        font_size = 16
        font = ImageFont.load_default(font_size)
        width, height = photo.size

        # Prepare branding.
        branding = f"{self.object} - Amateur Astro Image"

        # Compute branding size and position.
        margin = 10
        textwidth = draw.textlength(branding, font)
        x = width - textwidth - margin
        y = height - font_size - margin
        draw.text((x, y), branding, (255, 255, 255), font=font)

        # Update image.
        photo.save(self.image.path)
    

class Request(models.Model):
    """
    Request: The class defines how requests are saved in the db.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    sent_time = models.DateTimeField(editable=False)


    # The method defines how each request appears in the admin section.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.sent_time.astimezone(current_zone)
        
        # Return the correct string.
        return f"{self.first_name} {self.last_name} on {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The method saves the requests with the correct timestamp.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.sent_time = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comment: Model for storing user comments on astronomical images
    """
    image = models.ForeignKey(AstroImage, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.created_at = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)
    
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.created_at.astimezone(current_zone)

        # Return the correct string.
        return f"Comment by {self.name} on {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"
