""" Define the structure of stored data """
from django.db import models
from monetary.models import Accounts


class Companies(models.Model):
    """
        Save companies names
    Attributes:
        name:

    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:  # pylint: disable=R0903
        """ Sorted by name field """
        db_table = "companies"
        ordering = ["name",]

    def save(self, *args, **kwargs):
        self.name = self.name.upper()

        super().save(*args, **kwargs)

    def __str__(self):
        """ String for representing the ModelName object """
        return str(self.name)

    objects = models.Manager()


class Categories(models.Model):
    """
        Save category description
    Attributes:
        description:

    """
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:  # pylint: disable=R0903
        """ String for representing the ModelName object """
        db_table = "categories"
        ordering = ["description",]

    def __str__(self):
        """ Sorted by name field """
        return str(self.description)

    def save(self, *args, **kwargs):
        self.description = self.description.upper()

        super().save(*args, **kwargs)

    objects = models.Manager()
