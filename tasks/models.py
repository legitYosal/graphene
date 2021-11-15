from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class TaskStatus(models.TextChoices):
        NOTSTARTED = 'NOTSTARTED', _('Not started')
        INPROGRESS = 'INPROGRESS', _('In progress')
        DONE = 'DONE', _('Finished')

    status = models.CharField(max_length=16, choices=TaskStatus.choices, default=TaskStatus.NOTSTARTED)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self, ):
        return self.title

    class Meta:
        ordering = ['-created_at']