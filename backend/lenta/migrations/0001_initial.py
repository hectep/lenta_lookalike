# Generated by Django 2.1.4 on 2019-07-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='URL')),
                ('is_parsed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('url', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='URL')),
                ('header', models.CharField(max_length=200, verbose_name='Header')),
                ('body', models.CharField(max_length=4000, verbose_name='Body')),
                ('image', models.ImageField(default='default/default_news_image.jpg', upload_to='', verbose_name='Image')),
                ('original_date', models.DateTimeField(verbose_name='Date posted on lenta.ru')),
                ('post_date', models.DateTimeField(verbose_name='Date posted on this site')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
