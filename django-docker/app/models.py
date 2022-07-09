from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    
    class Meta:
        abstract = True

@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class Post(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField('Create data', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(BaseModel):
    text = models.CharField(max_length=100)
    date = models.DateTimeField('Create data', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
