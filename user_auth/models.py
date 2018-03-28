from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __unicode__(self):
        if self.last_name and self.first_name:
            return u'%s %s' % (self.first_name, self.last_name)
        else:
            return self.username
