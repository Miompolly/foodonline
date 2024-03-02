from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile



    

@receiver(post_save,sender=User)
def post_save_create_profile_reciever(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('create the user profile')
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if it is not exists
            UserProfile.objects.create(user=instance)
            print('User not exist but created one')            

        print('User is updated')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'User is being created')

