# AI Coding Agent Instructions for Amateur Astro Image Django Project

## Project Overview
This is a Django web application for displaying amateur astronomical images. It features image galleries with comments, contact forms, and automated image processing (thumbnails, watermarks).

## Architecture
- **Main App**: `mainsite` - handles all user-facing functionality
- **Models**: `AstroImage` (core image model with ImageKit processing), `Request` (contact submissions), `Comment` (image comments)
- **Key Dependencies**: Django ImageKit (thumbnail generation), Lightbox2 (gallery viewing), django-simple-captcha (form protection)

## Critical Workflows
- **Setup**: Create `.env` file in `astro_site/astro_site/` with database credentials, SECRET_KEY, TIMEZONE, DEBUG_SET, HTTPS
- **Database**: Use MariaDB/MySQL; run `python manage.py migrate --run-syncdb` then `createsuperuser`
- **Development Server**: `python manage.py runserver` or `python manage.py runserver_plus --cert-file cert.pem --key-file key.pem` (HTTPS)
- **Image Upload**: Upload via Django admin; images auto-processed with watermarks and thumbnails

## Code Patterns
- **Views**: Class-based views that add `title` and `path` to context for navigation (see `views.py`)
- **Image Processing**: Use ImageKit specs for thumbnails; watermarking happens in `AstroImage.save()` method
- **Forms**: Include captcha fields; custom error messages defined in `Meta.error_messages`
- **Search**: Implemented in `AstroImageList` using Django Q objects for multi-field search
- **Timezones**: Always convert UTC to local timezone using `pytz.timezone(settings.TIME_ZONE)` (see model `__str__` methods)

## Conventions
- **File Structure**: Static files in `static/`, media uploads in `bucket/`, processed static in `staticfiles/`
- **URLs**: Named patterns like `astroimage-details` for image detail pages
- **Templates**: Located in `templates/mainsite/`; base template in `templates/base.html`
- **Security**: CSP enabled via Django's built-in security features; session/CSRF cookies secured when HTTPS=True

## Key Files
- `astro_site/mainsite/models.py`: Image processing logic and watermarking
- `astro_site/mainsite/views.py`: All page views and search implementation
- `astro_site/astro_site/settings.py`: Environment-based configuration and SECURE_CSP rules
- `requirements.txt`: Full dependency list including Django 6.0

## Common Tasks
- Adding new image fields: Update `AstroImage` model, regenerate thumbnails if needed
- Modifying forms: Add captcha field and error messages in `forms.py`
- Changing image display: Update ImageKit processors in models for new sizes</content>
<parameter name="filePath">/home/nathan/Documents/amateurastroimage-django/.github/copilot-instructions.md