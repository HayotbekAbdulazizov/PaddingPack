from re import template
from .models import *
from django.views.generic import DetailView, TemplateView, View
from django.shortcuts import redirect, render
from .tg_sender import telegram_bot_sendphoto, telegram_bot_sendtext
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

class HomePageView(View):
	def get(self,request):
		context = {
			'status':200,
			'products': Product.objects.all(),
			'categories': Category.objects.all(),
			'creators':Creator.objects.all(),
		}		
		return render(request, 'index.html', context)

	def post(self, request):
		name = request.POST["name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		message  = request.POST["message"]
		client_message = ClientMessage.objects.create( name=name, phone=phone, email=email, message=message)
		telegram_bot_sendtext(f"  ClientMessage  \n Name: {name} \n Email :  {email}  \n Phone: +{phone} \n Link: https://paddingpack.uz/admin/main/clientmessage/{client_message.id}/change")
		messages.success(request, _("Your message was successfully submitted, please wait our call !"))
		
		return redirect(f'/') 




# About Company 
class AboutPageView(View):
	def get(self, request):
		context={
			'about_items':AboutItem.objects.all()
		}
		return render(request, 'about.html', context)



# Category DetailPage
class CategoryDetailView(DetailView):
	model = Category
	template_name = "category_detail.html"




# ProductDetailPage
class ProductDetailView(View):
	def get(self, request, pk):
		context = {
			'object':Product.objects.get(id=pk),
		}
		return render(request, 'product_detail.html', context)

	def post(self,request, pk):
		product = Product.objects.get(id=pk)
		additional_data = f""
		if product.form_input.all().count():
			for input_value in product.form_input.all():
				data = ''
				try:
					data = f" {input_value.name} : {request.POST[input_value.name]} \n"
				except:
					data= f"{input_value.name} : Not Given !"
				finally:
					additional_data += data
					 	
		amount = request.POST['amount']
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		message = request.POST['message']
	
		order = Order.objects.create(product=product, amount=amount, name=name, phone=phone, email=email, message=message, additional_info=additional_data)
		telegram_bot_sendtext(f"  \n  Product: {product.name} \n Name :  {name} \n Amount: {amount} \n Phone: {phone} \n Link: https://paddingpack.uz/admin/main/order/{order.id}/change")

		messages.success(request, _("Your order was successfully submitted, please wait our call ! !"))
		return redirect(f'/product/{pk}') 





# 404 Error Page
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)



# ERROR
class ErrorPageView(TemplateView):
	template_name = '404.html'