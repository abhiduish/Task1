# Generated by Django 3.1.7 on 2021-04-05 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('voucher', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('facevalue', models.IntegerField()),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob', models.IntegerField()),
                ('admi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mob_set', to='Abhi.admin')),
            ],
        ),
    ]
