from django.db import models
from PIL import Image
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Category, self).save(*args, **kwargs)

        if self.image:
            self.resize(self.image, 350, 200)

    def resize(self, image, width, height):
        img = Image.open(image.path)
        size = (width, height)
        img = img.resize(size)
        img.save(image.path)


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    count_in_stock = models.IntegerField(default=15)

    views = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)
    details = models.TextField()

    image = models.ImageField(upload_to='shop', blank=True, null=True)
    image2 = models.ImageField(upload_to='shop', blank=True, null=True)
    image3 = models.ImageField(upload_to='shop', blank=True, null=True)
    image4 = models.ImageField(upload_to='shop', blank=True, null=True)
    image5 = models.ImageField(upload_to='shop', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.images()

    def images(self):
        if self.image:
            self.resize(self.image, 500, 500)
        if self.image2:
            self.resize(self.image2, 500, 500)
        if self.image3:
            self.resize(self.image3, 500, 500)
        if self.image4:
            self.resize(self.image4, 500, 500)
        if self.image5:
            self.resize(self.image5, 500, 500)

    def resize(self, image, width, height):
        img = Image.open(image.path)
        size = (width, height)
        img = img.resize(size)
        img.save(image.path)

    def category_name(self):
        return self.category.name


class Showcase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    def name(self):
        return self.product.name

    def image(self):
        if self.product.image:
            return self.product.image.url
        else:
            return ''

    def details(self):
        return self.product.details[0:300]

    def product_id(self):
        return self.product.id


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)

    token = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.token}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.id}: {self.product.name}'

    def save(self, *args, **kwargs):
        self.name = self.product.name
        super(OrderItem, self).save(*args, **kwargs)
