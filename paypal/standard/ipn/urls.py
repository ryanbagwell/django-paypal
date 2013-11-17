try:
	#for Django >= 1.6
	from django.conf.urls import *
except:
	#for Django < 1.6
	from django.conf.urls.defaults import *

urlpatterns = patterns('paypal.standard.ipn.views',            
    url(r'^$', 'ipn', name="paypal-ipn"),
)