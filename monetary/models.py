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
        """ Sorted by name field """
        db_table = "monetary_accounts"
        ordering = ("name",)

    def save(self, *args, **kwargs):
        """ Save datas in uppercase """

        self.name = self.name.upper()
        self.description = self.description.upper()

        super().save(*args, **kwargs)

    def __str__(self):
        """ String for representing the ModelName object """

        return str(self.name)

    objects = models.Manager()
