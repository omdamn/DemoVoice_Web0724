# Generated by Django 2.2.3 on 2019-09-05 12:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190816_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Song', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.Voice')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
    ]
