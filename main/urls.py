from unicodedata import name
from django.urls import path,include
from .import views
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


app_name = 'main'

urlpatterns = [
	path('',views.HomePageView.as_view(), name='home'),
	path('about/',views.AboutPageView.as_view(), name='about'),
	path('category/<pk>', views.CategoryDetailView.as_view(), name='category_detail'),
	path('product/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
	

	path('error/', views.ErrorPageView.as_view(), name='error'),
	# path('get_order/', views.get_order, name='get_order'),
]
