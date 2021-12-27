import uuid
from django.db import models
from django.contrib.auth import get_user_model


def get_users_todos(user):
    try:
        return Todo.objects.filter(user=user)
    except:
        return None


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Todo(models.Model):
    # Priority choices
    PRIORITY_CHOICES = (
        ("bg-danger", "High"),
        ("bg-info", "Normal"),
        ("bg-warning", "Low"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    """
    due_date
    """

    def __str__(self):
        return self.description
