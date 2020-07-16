from django.db import models

class QuoteCategory(models.Model):
    title = models.CharField(max_length= 50)


class Quote(models.Model):
    quote = models.TextField()
    Author = models.CharField(max_length= 50)

    quote_category = models.ForeignKey(
        'QuoteCategory', on_delete = models.CASCADE
    )