from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is reqiored")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = None

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    picture = models.ImageField(upload_to="profile_pics", blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

