# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clubs(models.Model):
    idclubs = models.AutoField(db_column='idClubs', primary_key=True)  # Field name made lowercase.
    types = models.CharField(max_length=255)
    desc = models.TextField()
    contactemail = models.CharField(db_column='contactEmail', max_length=45)  # Field name made lowercase.
    contactemail2 = models.CharField(db_column='contactEmail2', max_length=45)  # Field name made lowercase.
    contactperson = models.CharField(db_column='contactPerson', max_length=45)  # Field name made lowercase.
    contactphone = models.CharField(db_column='contactPhone', max_length=15)  # Field name made lowercase.
    box = models.CharField(max_length=45)
    advisorid = models.ForeignKey('Professors', models.DO_NOTHING, db_column='advisorId')  # Field name made lowercase.
    affiliation = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Clubs'


class Corequisites(models.Model):
    courseid = models.OneToOneField('Courses', models.DO_NOTHING, db_column='courseId', primary_key=True)  # Field name made lowercase.
    coreqcourse = models.CharField(db_column='coreqCourse', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Corequisites'
        unique_together = (('courseid', 'coreqcourse'),)


class Corrections(models.Model):
    correctionid = models.AutoField(db_column='correctionId', primary_key=True)  # Field name made lowercase.
    rawtext = models.CharField(db_column='rawText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    correctiontext = models.CharField(db_column='correctionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tablenametocorrect = models.CharField(db_column='tableNameToCorrect', max_length=255, blank=True, null=True)  # Field name made lowercase.
    columnnametocorrect = models.CharField(db_column='columnNameToCorrect', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Corrections'


class Courses(models.Model):
    courseid = models.AutoField(db_column='courseId', primary_key=True)  # Field name made lowercase.
    dept = models.CharField(max_length=5)
    coursenum = models.IntegerField(db_column='courseNum')  # Field name made lowercase.
    termsoffered = models.CharField(db_column='termsOffered', max_length=13)  # Field name made lowercase.
    units = models.CharField(max_length=5)
    coursename = models.CharField(db_column='courseName', max_length=255)  # Field name made lowercase.
    raw_concurrent_text = models.TextField()
    raw_recommended_text = models.TextField()
    raw_prerequisites_text = models.TextField(blank=True, null=True)
    crosslistedas = models.CharField(db_column='crossListedAs', max_length=45)  # Field name made lowercase.
    raw_standing_text = models.CharField(max_length=45, blank=True, null=True)
    standing = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Courses'


class Officehours(models.Model):
    professors = models.OneToOneField('Professors', models.DO_NOTHING, db_column='Professors_id', primary_key=True)  # Field name made lowercase.
    ohroom = models.CharField(max_length=45)
    ohday = models.CharField(max_length=45)
    ohtime = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'OfficeHours'


class Polyratings(models.Model):
    id = models.IntegerField(primary_key=True)
    avgrating = models.FloatField(db_column='avgRating')  # Field name made lowercase.
    numratings = models.IntegerField(db_column='numRatings')  # Field name made lowercase.
    professors = models.ForeignKey('Professors', models.DO_NOTHING, db_column='Professors_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PolyRatings'


class Prerequisites(models.Model):
    courseid = models.OneToOneField(Courses, models.DO_NOTHING, db_column='courseId', primary_key=True)  # Field name made lowercase.
    prereqcourse = models.CharField(db_column='prereqCourse', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prerequisites'
        unique_together = (('courseid', 'prereqcourse'),)


class Professors(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=15)  # Field name made lowercase.
    research_interests = models.TextField(db_column='researchInterests')  # Field name made lowercase.
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Professors'


class Questionanswerformats(models.Model):
    idquestionformats = models.AutoField(db_column='idQuestionFormats', primary_key=True)  # Field name made lowercase.
    questionformat = models.CharField(db_column='questionFormat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    answerformat = models.CharField(db_column='answerFormat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userresponsetype = models.CharField(db_column='userResponseType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionAnswerFormats'


class Researchinterests(models.Model):
    interest = models.CharField(max_length=255)
    professors = models.OneToOneField(Professors, models.DO_NOTHING, db_column='Professors_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchInterests'
        unique_together = (('professors', 'interest'),)


class Sessions(models.Model):
    idsessions = models.AutoField(db_column='idSessions', primary_key=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTIme', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(max_length=7, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    questionasked = models.CharField(db_column='questionAsked', max_length=45, blank=True, null=True)  # Field name made lowercase.
    answergiven = models.CharField(db_column='answerGiven', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessions'


class Shortnames(models.Model):
    courseid = models.OneToOneField(Courses, models.DO_NOTHING, db_column='courseId', primary_key=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='shortName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShortNames'
        unique_together = (('courseid', 'shortname'),)
