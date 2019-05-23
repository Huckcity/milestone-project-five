# Generated by Django 2.2 on 2019-05-23 19:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('url', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=50.0, max_digits=5, null=True)),
                ('ticket_type', models.CharField(choices=[('Bug', 'Bug Report'), ('Feature', 'Feature Request')], max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='Pending', max_length=20)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('percent_complete', models.IntegerField(default=0)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_on', models.DateTimeField(default=datetime.datetime.now)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('contributed_on', models.DateTimeField(default=datetime.datetime.now)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.Ticket')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
