from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Expense(models.Model):
    class CategoryChoices(models.TextChoices):
        FOOD = 'Food'
        TRAVEL = 'Travel'
        UTILITIES = 'Utilities'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=100,
                                choices=CategoryChoices.choices, default=CategoryChoices.FOOD)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'expenses'
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-date']
