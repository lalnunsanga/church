# Generated by Django 4.2.16 on 2024-10-20 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methodist', '0005_category_author_category_date_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
