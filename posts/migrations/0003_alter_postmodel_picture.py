# Generated by Django 4.2.5 on 2023-11-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_user_id_postmodel_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/post_pictures/'),
        ),
    ]