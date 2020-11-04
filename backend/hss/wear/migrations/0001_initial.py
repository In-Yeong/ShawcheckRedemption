# Generated by Django 2.2.7 on 2020-11-04 08:17

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
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Coordi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordi_set', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Headwear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Outer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('style', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoordi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hat', models.IntegerField()),
                ('shirt', models.IntegerField()),
                ('pants', models.IntegerField()),
                ('outer', models.IntegerField()),
                ('shoes', models.IntegerField()),
                ('accessory', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyClothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Myclothes/%Y/%m/%d')),
                ('category', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeCoordi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordi_num', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
