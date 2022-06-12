"""fire a signal before a model is save """
from django.db.models.signals import pre_save

from django.contrib.auth.models import User


# function that let know when a user model is UPDATED
def updateUser(sender, instance, **kwargs):
    print('signal triggered')
    #check if the username is the same as the email and then if not so make it
    user = instance
    if user.email != '':
        # save the user with email as a username
        user.username = user.email

pre_save.connect(updateUser, sender=User)
# so when the user models is saved it will call the updateUser function



