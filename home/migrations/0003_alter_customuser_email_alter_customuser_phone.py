# Generated by Django 5.0.6 on 2024-05-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_dob_customuser_dob_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='+91987654321', max_length=15),
        ),
    ]
