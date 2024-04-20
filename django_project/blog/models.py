from django.db import models  # Importing the models module from Django
from django.utils import timezone  # Importing the timezone module from Django
from django.contrib.auth.models import User  # Importing the User model from Django's authentication system

# Create your models here.
class Post(models.Model):
    # Defining the Post model as a subclass of models.Model
    title = models.CharField(max_length=100)  # Title field for the post, limited to 100 characters
    content = models.TextField()  # Content field for the post, allowing for larger text
    date_posted = models.DateTimeField(default=timezone.now)  # Date and time when the post was created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model, each post belongs to a user
    # on_delete=models.CASCADE ensures that if the associated user is deleted, all related posts are also deleted

    def __str__(self):
        return self.title