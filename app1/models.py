from django.db import models

class user_data(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    # que = models.CharField(max_length=20) # remove this
    # anw = models.CharField(max_length=10) # remove this
    password = models.CharField(max_length=20)
    # validators=[MaxValueValidator(5)]
    adhar = models.CharField(max_length=12, default=0)
    image = models.ImageField(upload_to="static/assets/uploaded_images", default="")

    def __str__(self):
        return self.name

class complaint(models.Model):
    user = models.ForeignKey(user_data, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/assets/uploaded_images", default="")
    action = models.BooleanField(null=True)

class schemes(models.Model):
    s_id  = models.IntegerField()
    s_name  = models.CharField(max_length=50)
    s_detail  = models.CharField(max_length=100)

class notice(models.Model):
    n_name = models.CharField(max_length=100)
    n_date = models.DateField()
    n_detail = models.CharField(max_length=100)

class appointment(models.Model):
    fk = models.ForeignKey(user_data, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    purpose = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    action = models.BooleanField(null=True)