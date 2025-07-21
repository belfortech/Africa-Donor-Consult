"""
URL configuration for Donor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include


from AfricaConsult import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('AfricaConsult.urls')),
    path('', views.home, name='home'),  # Homepage
    path('about-us/', views.about_us, name='about_us'),
    path('our-services/', views.our_services, name='our_services'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('service-details/', views.service_details, name='service_details'),
    path('services/procurement-training/', views.procurement_training, name='procurement_training'),
    path('services/procurement-audit/', views.procurement_audit, name='procurement_audit'),
    path('services/fraud-risk/', views.fraud_risk, name='fraud_risk'),
    path('services/monitoring/', views.monitoring, name='monitoring'),
    path('services/implementation-audit/', views.implementation_audit, name='implementation_audit'),

    path('newsletter/', views.newsletter, name='newsletter'),

 
]