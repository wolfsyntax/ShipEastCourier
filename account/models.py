from django.db import models

# Create your models here.
from django.core.mail import send_mail
from django.contrib.auth.models import User

PARISH = (
    ('', 'Choose...'),
    ('St. Andrew', 'Kingston'),
    ('Portland', 'St. Thomas'),
    ('St. Catherine', 'St. Mary'),
    ('St. Ann', 'Manchester',),
    ('Clarendon', 'Hanover',),
    ('Westmoreland', 'St. James',),
    ('Trelawny', 'St. Elizabeth')
)

PARCEL_STATUS = (
    ('', 'Parcel Status'),
    ('pickup', 'Pickup'),
    ('on process', 'On Process'),
    ('on delivery', 'On Delivery'),
    ('delivered', 'Delivered'),
    

)
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    trn = models.CharField(max_length=10)
    address = models.CharField(max_length=254)

    district = models.CharField(max_length=254)
    #country = models.CharField(max_length=254)
    
    parish = models.CharField(choices=PARISH, max_length=15)
	
    description = models.CharField(max_length=255, blank=True)
#    document = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def save(self, *args, **kwargs): 
        #self.slug = slugify(self.title) 
        super(Profile, self).save(*args, **kwargs) 

    class Meta:
        db_table='Profile'
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profile"

class MailClient(models.Model):

    subject = models.CharField(max_length=255)
    message = models.TextField()
    attachment = models.FileField(null=True, blank=True)
    users = models.ManyToManyField(User, blank=False)

    send_it = models.BooleanField(default=False) #check it if you want to send your email
    
    def __str__(self):
        return self.subject

    def save(self):
       
    
    #    print("\n\nSubject: {}\n\n\n\n\n".format(self.users))
        super(MailClient, self).save() 
        
        if self.send_it:
            #First you create your list of users
            user_list = []

            #print("\n\n\n\nEmail Client\n\n\n{}\n\n\n\n".format(self.users.length))
            
            for u in self.users.all():
                user_list.append(u.email)
    
            send_mail(str(self.subject), str(self.message), 'support@shipeastcouriers.com', user_list, fail_silently=False)
            
        

    class Meta:
        
        verbose_name = "Email to send"
        verbose_name_plural = "Emails to send"
        db_table='MailClient'

class TrackingDetails(models.Model):

    trackcode = models.SlugField(max_length=32)
    courier = models.CharField(max_length=255)
    merchant = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    parcel_status = models.CharField(choices=PARCEL_STATUS, max_length=255)
    
    parcel_price = models.FloatField()
    shipping_fee = models.FloatField()
    
    date_shipped = models.DateTimeField()
    date_arrived = models.DateTimeField(null=True, blank=True) 
    
    user = models.ForeignKey(User,on_delete=models.CASCADE) 


    def __str__(self):
        return "{}:{}".format(self.courier, self.trackcode)

    class Meta:
        verbose_name = "Tracking Detail"
        verbose_name_plural = "Tracking Details"
        db_table='TrackingDetails'