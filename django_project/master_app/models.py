from datetime import datetime
from django.db import models
# Create your models here.
class user_master(models.Model):                
    userid =models.IntegerField(auto_created=True,primary_key=True,serialize=False,verbose_name="userid") 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)  
    password=models.CharField(max_length=50)    
    rolename=models.CharField(max_length=50)
    createdby =models.CharField(max_length=50)
    # jn_date=models.DateField(default='0000-00-00',null=True,blank=True)
    # lv_date=models.DateField(default='0000-00-00',null=True,blank=True)
    # dob=models.DateField(default='0000-00-00',null=True,blank=True)
    mail_id=models.CharField(max_length=50,null=True,blank=True)
    external_mail=models.CharField(max_length=50,null=True,blank=True)
    personal_mail=models.CharField(max_length=50,null=True,blank=True)
    mail_indi=models.CharField(max_length=50,null=True,blank=True)
    gndr=models.IntegerField(default=1)   
    crnt_sts=models.IntegerField(default=1)
    mgr=models.IntegerField(null=True,blank=True)
    blood_group=models.CharField(max_length=10,null=True,blank=True)
    phno=models.IntegerField(null=True,blank=True)
    loc=models.CharField(max_length=50,null=True,blank=True)    
    gl=models.CharField(max_length=60,null=True,blank=True)
    tl=models.IntegerField(null=True,blank=True)    
    company_id=models.IntegerField(null=True,blank=True)       
    timestamp=models.DateTimeField(default=datetime.now)
    delete1=models.IntegerField(default=0)
    marital_status=models.IntegerField(default=0)
    tms_status=models.IntegerField(default=0)
    ass_role=models.CharField(max_length=10,null=True,blank=True)
    qualification=models.CharField(max_length=20,default='SSC',null=True,blank=True)    
    # marriage_date=models.DateField(default='0000-00-00',null=True,blank=True)
    def __str__(self):
        return str(self.userid)
    class Meta:
        db_table="user_master"
    
