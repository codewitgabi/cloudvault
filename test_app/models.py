from django.db import models


class Picture(models.Model):
    image = models.ImageField()

    # ... other fields

    def __str__(self):
        return str(self.id)


