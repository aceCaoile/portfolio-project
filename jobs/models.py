from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()  # "auto_now_add" when True will auto fill the Date and Time with now...
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    body2 = models.TextField(default='', blank=True)
    image2 = models.ImageField(default=None, blank=True, upload_to='images/')

    body3 = models.TextField(default='', blank=True)
    image3 = models.ImageField(default=None, blank=True, upload_to='images/')

    body4 = models.TextField(default='', blank=True)
    image4 = models.ImageField(default=None, blank=True, upload_to='images/')

    body5 = models.TextField(default='', blank=True)
    image5 = models.ImageField(default=None, blank=True, upload_to='images/')

    body6 = models.TextField(default='', blank=True)
    image6 = models.ImageField(default=None, blank=True, upload_to='images/')

    body7 = models.TextField(default='', blank=True)
    image7 = models.ImageField(default=None, blank=True, upload_to='images/')

    body8 = models.TextField(default='', blank=True)
    image8 = models.ImageField(default=None, blank=True, upload_to='images/')

    body9 = models.TextField(default='', blank=True)
    image9 = models.ImageField(default=None, blank=True, upload_to='images/')

    def __str__(self):  # This is the name of the function used to display titles from the admin page
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')