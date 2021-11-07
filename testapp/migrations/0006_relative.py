# Generated by Django 3.2.9 on 2021-11-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20211107_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.CharField(max_length=20, null=True)),
                ('details', models.TextField(max_length=500, null=True)),
                ('cousin', models.ManyToManyField(to='testapp.Test')),
            ],
        ),
    ]
