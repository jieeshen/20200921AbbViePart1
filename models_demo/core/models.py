from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AdCampaign(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date}/{self.end_date}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    campaign = models.OneToOneField(AdCampaign, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    books = models.ManyToManyField(Book)  # can be on either end

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

