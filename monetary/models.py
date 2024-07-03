""" Define the structure of stored data """

from django.db import models


class Accounts(models.Model):
    """
        Model Accounts
    Attributes:
        name:
        description:

    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=240)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:  # pylint: disable=R0903
        """Sorted by name field"""

        db_table = "monetary_accounts"
        ordering = ("name",)

    def save(self, *args, **kwargs):
        """Save datas in uppercase"""
        self.name = self.name.upper()
        self.description = self.description.upper()

        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the ModelName object"""
        return str(self.name)

    objects = models.Manager()


class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    out_account = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="outgoing_transfers"
    )
    in_account = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="incoming_transfers"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        db_table = "monetary_transfers"
        ordering = ("date", "out_account", "in_account")

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)

    def __str__(self):
        return str(f"{self.out_account} - {self.in_account} - R$ {self.value}")

    objects = models.Manager()
