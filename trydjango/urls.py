"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import reg_form
from pages.views import about_us
from pages.views import contact
from pages.views import save_contact
from pages.views import save_reg
from pages.views import find
from pages.views import results
from django.conf import settings
from django.conf.urls.static import static

# from . import views
urlpatterns = [
    path('', home_view, name='home', ),
    path('admin/', admin.site.urls),
    path('registration_form/', reg_form, name='profile'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('savecontact/', save_contact, name='save_contact'),
    path('savereg/',save_reg, name='save_reg'),
    path('finddonor/',find,name='finddonor'),
    path('results/', results, name = 'results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

