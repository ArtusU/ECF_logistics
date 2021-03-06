# Generated by Django 3.1.3 on 2020-11-20 12:25

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
            name='Delivery_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=10)),
                ('comments', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('occupation', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('refereed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.referrer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('F&VBox', 'F&VBox'), ('Invoice', 'Invoice'), ('Essential', 'Essential'), ('T&M', 'T&M'), ('Other', 'Other')], max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('day_created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('product_category', models.ManyToManyField(to='cms.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('Placed', 'Placed'), ('Approved', 'Approved'), ('Unstaged', 'Unstaged'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('SO', 'Standing Order')], max_length=100)),
                ('delivery_day', models.CharField(blank=True, choices=[('Unstaged', 'Unstaged'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100)),
                ('run', models.CharField(blank=True, choices=[('pickup', 'pickup'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_address', to='cms.delivery_address')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.product')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.recipient')),
                ('referrer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.referrer')),
            ],
        ),
        migrations.AddField(
            model_name='delivery_address',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.recipient'),
        ),
    ]
