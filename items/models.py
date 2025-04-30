from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Save the object to assign it an ID if it's new
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # If it's new and no order is set, set order = ID and save again
        if is_new and self.order is None:
            self.order = self.pk
            super().save(update_fields=['order'])  # Only update the order field
