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
        """Sorted by name field"""

        db_table = "companies"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        self.name = self.name.upper()

        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the ModelName object"""
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
        """String for representing the ModelName object"""

        db_table = "categories"
        ordering = ["description"]

    def __str__(self):
        """Sorted by name field"""
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
    value = models.DecimalField(max_digits=10, decimal_places=2)
    in_out = models.BooleanField(default=False)
    ordering = models.IntegerField(default=0)
    obs = models.TextField(max_length=120, blank=True)

    class Meta:  # pylint: disable=R0903
        """Sorted by name field"""

        db_table = "transactions_registries"
        ordering = ["-date", "-ordering"]

    def __str__(self):
        """String for representing the ModelName object"""
        return str(f"{self.companies} - {self.id}")

    def save(self, *args, **kwargs):
        self.obs = self.obs.upper()

        super().save(*args, **kwargs)

    objects = models.Manager()


class RegistryItens(models.Model):
    """
        Saves items from registries
    Attributes:
        description:

    """

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)
    brand = models.CharField(max_length=20, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    unitary = models.DecimalField(max_digits=10, decimal_places=2)
    favored = models.CharField(max_length=20, null=True)
    registry = models.ForeignKey(Registries, on_delete=models.CASCADE)

    class Meta:  # pylint: disable=R0903
        """Sorted by name field"""

        db_table = "transactions_itens"
        ordering = ["description"]

    def __str__(self):
        """String for representing the ModelName object"""
        return str(f"{self.description} - {self.registries}")

    def save(self, *args, **kwargs):
        self.description = self.description.upper()

        super().save(*args, **kwargs)

    objects = models.Manager()


class Payments(models.Model):
    """
    Saves payments from registries
    """

    id = models.AutoField(primary_key=True)
    registry = models.ForeignKey(Registries(), on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:  # pylint: disable=R0903
        """Sorted by name field"""

        db_table = "transactions_payments"
        ordering = ["date", "registry"]

    def __str__(self):
        """String for representing the ModelName object"""
        return str(self.registry)

    objects = models.Manager()


class Methods(models.Model):
    """
    Saves methods payments
    """

    id = models.AutoField(primary_key=True)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:  # pylint: disable=R0903
        """Sorted by name field"""

        db_table = "transactions_methods"
        ordering = ["payment"]

    def __str__(self):
        """String for representing the ModelName object"""
        return str(f"{self.account} - {self.payment}")

    objects = models.Manager()
