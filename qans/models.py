# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
import datetime

class AuthGroup(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    #id = models.IntegerField(primary_key=True)
    group = models.ForeignKey('AuthGroup')
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser')
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(unique=True, max_length=200)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    #id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey('AuthGroup')
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class BooksUser(models.Model):
    #id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    class Meta:
        db_table = u'books_user'

class DjangoAdminLog(models.Model):
    #id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=200)
    model = models.CharField(unique=True, max_length=200)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    #id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class QansUserregistration(models.Model):
    #id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    dob = models.DateField()
    email = models.CharField(max_length=225)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    addr = models.TextField()
    dateofregistration = models.DateTimeField(default=datetime.datetime.now)
    country = models.CharField(max_length=150)
    class Meta:
        db_table = u'qans_userregistration'

class QansQuestion(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(QansUserregistration)
	question = models.TextField()
	dateofquestion = models.DateTimeField(default=datetime.datetime.now)
	class Meta:
		db_table = u'qans_question'

class QansAnswer(models.Model):
	user = models.ForeignKey(QansUserregistration)
	quser = models.ForeignKey(QansQuestion)
	answer = models.TextField()
	dateofanswer = models.DateTimeField(default=datetime.datetime.now)
	class Meta:
		db_table = u'qans_answer'

'''class RegistrationRegistrationprofile(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    activation_key = models.CharField(max_length=120)
    class Meta:
        db_table = u'registration_registrationprofile'
'''
