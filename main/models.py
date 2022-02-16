from pyexpat import model
from django.db import models
from django.urls import reverse

from parler.models import TranslatableModel, TranslatedFields






# Product Model
class Product(TranslatableModel):
    Sizings = [    ('Kg', 'Kg'),    ('M', 'M'),    ('M²', 'M²'),]
    translations = TranslatedFields(
        name=models.CharField("Name", max_length=200),
        slug=models.SlugField("Slug"),
        price = models.CharField('price', max_length=100, blank=True, ),
        sizing = models.CharField('Sizing', max_length=200, choices=Sizings, blank=True),
        image = models.ImageField('Image', upload_to='product_images/', blank=True),
        description=models.TextField(),
        meta={"unique_together": (("slug", "language_code"),),},
    )
    category = models.ForeignKey("Category", null=True, related_name='products',blank=True, on_delete=models.CASCADE)
    corrugated = models.BooleanField('Korobka ', default=False, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"


# Product Images
class ProductImages(TranslatableModel):
    translations = TranslatedFields(
        image = models.ImageField('Product_image', upload_to='product_images/'),
    )
    product = models.ForeignKey("Product", related_name="images", null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        return f"{self.product.name}"

# Additional Form model
class AdditionalFormValue(TranslatableModel):
    INPUT_TYPES = [ ('text', 'TEXT'),    ('number', 'NUMBER')]
    product = models.ManyToManyField("Product", related_name='form_input',  blank=True)

    translations = TranslatedFields(
        name = models.CharField('Name', max_length=200, blank=True),
        placeholder = models.CharField('Placeholder', max_length=300, blank=True),
        type = models.CharField('Type', max_length=20, choices=INPUT_TYPES , blank=True),
    )

    def __str__(self):
        return self.name











# Category Model    
class Category(TranslatableModel): 
    translations = TranslatedFields(
        name=models.CharField("Name", max_length=200),
        slug = models.SlugField('*'),
        image = models.ImageField('Category image', upload_to='category_images/', blank=True),
        description = models.TextField('Description'),
        additional = models.CharField('Additional', max_length=500, blank=True)
    )
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


# AddBlockItem foreignkey for Category
class AddBlockItem(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField("Name", max_length=1700, blank=True),
    )
    category = models.ForeignKey("Category",related_name='items' ,null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "AddBlockItem"
        verbose_name_plural = "AddBlockItems"

    def __str__(self):
        return f"{self.name}"


class CategoryImage(TranslatableModel):
    translations = TranslatedFields(
        image = models.ImageField('Category_Image', upload_to='category_images/'),
    )
    category = models.ForeignKey("Category", null=True, related_name='images' , blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category Image"
        verbose_name_plural = "Category Images"

    def __str__(self):
        return f"{self.category.name}"









class AboutItem(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField('Title', max_length=300, blank=True),
        body = models.TextField("Body", blank=True),
        image = models.ImageField("Image", upload_to="about_images/" ,blank=True),
    )

    class Meta:
        verbose_name = "AboutItem"
        verbose_name_plural = "AboutItems"

    def __str__(self):
        return f"{self.id}"











# ClientMessage class
class ClientMessage(models.Model):
    name = models.CharField("Name", max_length=300)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Phone", max_length=30, blank=True)
    message = models.TextField('Message', blank=True)
    date = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client Message'
        verbose_name_plural = 'Client Messages'




# Website creator model
class Creator(models.Model):
    work = models.CharField('Work', max_length=400, blank=True)
    name = models.CharField('Name', max_length=200, blank=True)
    url = models.URLField('URL', max_length=200, blank=True)

    def __str__(self):
        return self.name



# class of client Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    amount = models.PositiveIntegerField('Amount')
    name = models.CharField('Name', max_length=200)
    phone = models.CharField('Phone Number', max_length=200)
    email = models.EmailField('Email', max_length=200, blank=True)
    message = models.TextField('Text', blank=True)
    additional_info = models.TextField('Additional Data', blank=True)    
    date = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
