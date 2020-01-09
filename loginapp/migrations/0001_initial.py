# Generated by Django 3.0 on 2020-01-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='attendances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('status_h1', models.CharField(max_length=200)),
                ('status_h2', models.CharField(max_length=200)),
                ('status_h3', models.CharField(max_length=200)),
                ('status_h4', models.CharField(max_length=200)),
                ('status_h5', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='fac_leave_management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('from_date', models.CharField(max_length=200)),
                ('To_date', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='marksubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('assess_no', models.CharField(max_length=200)),
                ('max_mark', models.CharField(max_length=200)),
                ('subject_1', models.CharField(max_length=200)),
                ('subject_2', models.CharField(max_length=200)),
                ('subject_3', models.CharField(max_length=200)),
                ('subject_4', models.CharField(max_length=200)),
                ('subject_5', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stu_leave_management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('from_date', models.CharField(max_length=200)),
                ('To_date', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='studentregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=200)),
                ('admission_date', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('guardian', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
