from django.db import models

# Create a blog model here.
# title
# pub_date
# body
# image


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()  # "auto_now_add" when True will auto fill the Date and Time with now...
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):  # This is the name of the function used to display titles from the admin page
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Add the blog app to the settings

# Create a migration

# Migrate

# Add to the admin
