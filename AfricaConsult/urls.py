from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
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


    
