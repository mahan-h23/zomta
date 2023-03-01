from django.db import models


class HomePageContent(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Home Page Content'


class BlogContent(models.Model):
    homepage = models.ForeignKey(HomePageContent, on_delete=models.CASCADE,related_name='home_content')
    text_content = models.TextField(null=True, blank=True)
    img_field = models.ImageField(upload_to='homepage', null=True, blank=True)

