from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth import get_user_model

class Board(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.TimeField(default=datetime.now())
    updated_at = models.TimeField(default=datetime.now())
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model(), related_name='boards')

    def __str__(self):
        return self.name

