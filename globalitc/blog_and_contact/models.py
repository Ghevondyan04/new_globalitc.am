from django.db import models


class NewsHeader(models.Model):
    news_header_title = models.CharField(max_length=50)
    news_header_context = models.CharField(max_length=500)
    news_header_image = models.ImageField(upload_to="NewsHeaderImages")

    def __str__(self):
        return f"{self.news_header_title}"

    class Meta:
        verbose_name = "Նորության Էջի Վերևի հատված"
        verbose_name_plural = "Նորության Էջի Վերևի հատված"


class Offer(models.Model):
    offer_title = models.CharField(max_length=50)
    offer_context = models.CharField(max_length=500)
    offer_image = models.ImageField(upload_to="OfferImages")
    created_at = models.DateField(auto_now_add=True)
    last_date = models.DateField()
    in_home_page = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.offer_title}"

    class Meta:
        verbose_name = "առաջարկ"
        verbose_name_plural = "Առաջարկներ"


class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_context = models.CharField(max_length=500)
    news_image = models.ImageField(upload_to="NewsImages")
    created_at = models.DateField(auto_now_add=True)
    in_home_page = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.news_title}"

    class Meta:
        verbose_name = "նորություն"
        verbose_name_plural = "Նորություններ"


class CallOrder(models.Model):
    customer_name = models.CharField(max_length=50)
    call_date = models.CharField(max_length=20)
    customer_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer_name} {self.customer_number}"

    class Meta:
        verbose_name = "Զանգի պատվեր"
        verbose_name_plural = "Զանգի պատվերներ"


class ContactWithUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Կապ"
        verbose_name_plural = "Կապեր"


class Subscribe(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)
