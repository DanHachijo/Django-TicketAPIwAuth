# Generated by Django 4.0.2 on 2022-09-28 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('companyID', models.CharField(blank=True, max_length=10, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('suite', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_prospect', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('japanese_name', models.CharField(blank=True, max_length=30, null=True)),
                ('storeID', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('suite', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_prospect', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.company')),
            ],
            options={
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.company')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.store')),
            ],
            options={
                'verbose_name_plural': 'Customer Contacts',
            },
        ),
    ]