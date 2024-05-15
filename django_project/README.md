# Django snippets

## Note
- Dealing with bootstrap/uni_form.html error ensure that django-crispy-forms==1.14.0 is installed using ```pip install django-crispy-forms==1.14.0```

- ensure you migrate to make changes in the db
```
from django.core.paginator import Paginator
>>> posts = ['1', '2', '3', '4', '5']
>>> p = Paginator(posts, 2)
>>> p.num_pages
3
>>> for page in p.page_range:
...     print(page)
... 
1
2
3
>>> p1 = p.page(1)
>>> p1
<Page 1 of 3>
>>> p1.number
1
>>> p1.object_list
['1', '2']
>>> p1.has_previous()
False
>>> p1.has_next()
True
>>> p1.next_page_number()
2
>>>
```

``` http://127.0.0.1:8000/?page=5 ``` access 5th page after pagination

## Users
- Login and logout - ensures that users can login or logout
- Profile picture - the users can log their profiles and change their profiles