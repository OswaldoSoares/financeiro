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


class Registries(models.Model):
    """
        Saves registry of incoming and outgoing movements
    Attributes:
        favored:
        obs:

    """
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    companies = models.ForeignKey(Companies, on_delete=models.CASCADE)
    category_n1 = models.ForeignKey(
        Categories, related_name="category_n1", on_delete=models.CASCADE
    )
    category_n2 = models.ForeignKey(
        Categories, related_name="category_n2", on_delete=models.CASCADE
    )
    category_n3 = models.ForeignKey(
        Categories, related_name="category_n3", on_delete=models.CASCADE
    )
    favored = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    ordering = models.IntegerField(default=0)
    obs = models.TextField(max_length=120)

    class Meta:  # pylint: disable=R0903
        """ Sorted by name field """
        db_table = "transactions_registries"
        ordering = ["date", "ordering", ]

    def __str__(self):
        """ String for representing the ModelName object """
        return str(self.companies)

    def save(self, *args, **kwargs):
        self.favored = self.favored.upper()
        self.obs = self.obs.upper()

        super().save(*args, **kwargs)

    objects = models.Manager()
