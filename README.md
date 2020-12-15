# Blog-Post

* create a Blog_App project and blog app.

* create a templates and static folder in blog app directory.

* create a base, home, about html pages.

* create a base template required for our website in base.html page.

* Add a bootstrap and js content to base.html page.

* Extend the base.html page content to other html pages.

* Create a view for home and about page in views.py file.

* Add a url mapping for home and about page in urls.py file.

* Create a css file in static folder and load the static files in html pages.

* Run the server and make sure evrything working fine.

* Run a migrations to cretae auth_user table.

* Create a super user using python manage.py createsuperuser

* Verify admin page is working or not.

* Create a Post model in models.py file and make migrations.

* Create a users app and create a register,login,logout views.

* For registration create a custom registration form inherting the inbuilt UserCreationForm.

* For login and logout import a inbuilt class based Login and Logout views.

* Install a crispy forms and mention crispy_forms in installed apps.

* Mention CRISPY_TEMPLATE_PACK='bootstrap4' in settings.py file.

* Add a LOGIN_REDIRECT_URL in settings.py file.

* Create a Profile model with one field as user which has one to one relationship with django User model and another field as profile pic.

* Media root and Media url settings are added in settings.py file.

* Profile view is added in views.py file with login decorator.

* Note: We will access image based on URL(user.profile.image.url).

* MEDIA_ROOT (media folder) is the directory where the uploaded files are stored. For performance reason we store the images in file system not on database.

* MEDIA_URL is te way how we access the media files through browser.For ex: /media/profile_pic/default.jpg.

* Through user.profile.image.url we can access image in profile.html.

```
{% block content %}
  <div class="content-section">
  <div class="media">
    <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
    <div class="media-body">
      <h2 class="account-heading">{{ user.username }}</h2>
      <p class="text-secondary">{{ user.email }}</p>
    </div>
  </div>
  <!-- FORM HERE -->
  </div>
{% endblock %}
```

* We have add media root to url patterns only when it is in DEBUG mode.

```
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

* For every new user created they should automatically get user profile which will include default profile pic

* Inside users app create signals.py file.

* we should get a post_save signal when user gets created.

* User model is the sender and also we need receiver to perform task.
```
from django.dispatch import receiver
```

* For creating profile
```
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
```
* For saving the profile
```

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
```

* In apps.py file create a ready method
```
def ready(self):
        import users.signals
```
