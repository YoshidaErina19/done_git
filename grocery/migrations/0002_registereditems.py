# Generated by Django 4.0.4 on 2022-06-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_items', models.CharField(max_length=20, verbose_name='登録したアイテム')),
            ],
            options={
                'verbose_name_plural': 'RegisteredItems',
            },
        ),
    ]
