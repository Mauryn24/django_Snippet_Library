# Django Tutorial

## Admin Page
python manage.py createsuperuser

- Must have created db migrations
- code
  ```python manage.py makemigrations```
  then run
  ```python manage.py migrate```
  rerun
  ```python manage.py createsuperuser```

## Database
open models.py and create your function eg


from django.db import models  # Importing the models module from Django
from django.utils import timezone  # Importing the timezone module from Django
from django.contrib.auth.models import User  # Importing the User model from Django's authentication system

<!-- Create your models here. -->
class Post(models.Model):
    # Defining the Post model as a subclass of models.Model
    title = models.CharField(max_length=100)  # Title field for the post, limited to 100 characters
    content = models.TextField()  # Content field for the post, allowing for larger text
    date_posted = models.DateTimeField(default=timezone.now)  # Date and time when the post was created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model, each post belongs to a user
    # on_delete=models.CASCADE ensures that if the associated user is deleted, all related posts are also deleted

- make migrations
  ```python manage.py makemigrations```
- the run
    ```python manage.py migrate```

- viewing exact sql code
```python manage.py sqlmigrate app_name number```
eg
```python manage.py sqlmigrate blog 0001```

### commmands to run in terminal
- running python shell on cmd
   ```python manage.py shell```
   - this creates an interactive console. Run the following commands
    ```from blog.models import Post```
    ```from django.contrib.auth.models import User```
    ```User.objects.all() ```
    ```User.objects.first()```
    ```user = User.objects.filter(username='ashley').first()```
    <!-- check attributes -->
    eg ```user.id```
    <!-- creating posts -->
    ```post_1 = Post(title='Blog 1', content='First Content', author=user)```
    <!-- querying -->
    ```Post.objects.all()```
    <!-- saving to db -->
    ```post_1.save()```
    <!--  -->
    ```post = Post.objects.first()```
    <!-- getting all posts by a certain user -->
    .modelname_set
    eg ```user.post_set```
    ```user.post_set.all()```
    <!-- creating a post without need to save -->
    ```user.post_set.create(title='Blog 4', content='Four')```

### back to project
in the views.py have something like this
```
from django.shortcuts import render  # Importing the render function from Django shortcuts
from .models import Post  # Importing the Post model from the current directory's models module


 <!-- Create your views here. -->

def home(request):
    # Retrieve all posts from the database using the Post model
    context = {
        'posts': Post.objects.all()  # Querying all Post objects from the database
    }
    # Render the home.html template with the retrieved posts
    return render(request, 'blog/home.html', context)

def about(request):
    # Render the about.html template with the title 'About page'
    return render(request, 'blog/about.html', {'title': 'About page'})
```
<!-- register your model in the admin.py file -->
```
    from django.contrib import admin
from .models import Post

<!-- Register your models here. -->
admin.site.register(Post)
```
