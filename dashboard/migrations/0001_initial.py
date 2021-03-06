# Generated by Django 3.0 on 2019-12-11 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('idclubs', models.AutoField(db_column='idClubs', primary_key=True, serialize=False)),
                ('types', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('contactemail', models.CharField(db_column='contactEmail', max_length=45)),
                ('contactemail2', models.CharField(db_column='contactEmail2', max_length=45)),
                ('contactperson', models.CharField(db_column='contactPerson', max_length=45)),
                ('contactphone', models.CharField(db_column='contactPhone', max_length=15)),
                ('box', models.CharField(max_length=45)),
                ('affiliation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Clubs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Corrections',
            fields=[
                ('correctionid', models.IntegerField(db_column='correctionId', primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Corrections',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseid', models.IntegerField(db_column='courseId', primary_key=True, serialize=False)),
                ('dept', models.CharField(max_length=5)),
                ('coursenum', models.IntegerField(db_column='courseNum')),
                ('termsoffered', models.CharField(db_column='termsOffered', max_length=9)),
                ('units', models.IntegerField()),
                ('coursename', models.CharField(db_column='courseName', max_length=255)),
                ('concurrent', models.CharField(max_length=45)),
                ('recommended', models.CharField(max_length=45)),
                ('crosslistedas', models.CharField(db_column='crossListedAs', max_length=45)),
                ('standing', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'Courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Polyratings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('avgrating', models.FloatField(db_column='avgRating')),
                ('numratings', models.IntegerField(db_column='numRatings')),
            ],
            options={
                'db_table': 'PolyRatings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_column='firstName', max_length=45)),
                ('lastname', models.CharField(db_column='lastName', max_length=45)),
                ('phonenumber', models.CharField(db_column='phoneNumber', max_length=15)),
                ('researchWants', models.CharField(db_column='research wants', max_length=255)),
                ('email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Professors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Responseformats',
            fields=[
                ('idquestionformats', models.IntegerField(db_column='idQuestionFormats', primary_key=True, serialize=False)),
                ('questionformat', models.CharField(blank=True, db_column='questionFormat', max_length=255, null=True)),
                ('answerformat', models.CharField(blank=True, db_column='answerFormat', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ResponseFormats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Corequisites',
            fields=[
                ('courseid', models.OneToOneField(db_column='courseId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.Courses')),
                ('coreqcourse', models.CharField(db_column='coreqCourse', max_length=255)),
            ],
            options={
                'db_table': 'Corequisites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Officehours',
            fields=[
                ('professors', models.OneToOneField(db_column='Professors_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.Professors')),
                ('ohroom', models.CharField(max_length=45)),
                ('ohday', models.CharField(max_length=45)),
                ('ohtime', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'OfficeHours',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prerequisites',
            fields=[
                ('courseid', models.OneToOneField(db_column='courseId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.Courses')),
                ('prereqcourse', models.CharField(db_column='prereqCourse', max_length=255)),
            ],
            options={
                'db_table': 'Prerequisites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Researchinterests',
            fields=[
                ('interest', models.CharField(max_length=255)),
                ('professors', models.OneToOneField(db_column='Professors_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.Professors')),
            ],
            options={
                'db_table': 'ResearchInterests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shortnames',
            fields=[
                ('courseid', models.OneToOneField(db_column='courseId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.Courses')),
                ('shortname', models.CharField(db_column='shortName', max_length=255)),
            ],
            options={
                'db_table': 'ShortNames',
                'managed': False,
            },
        ),
    ]
