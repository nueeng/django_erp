# Generated by Django 4.2 on 2023-04-10 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='코드')),
                ('name', models.CharField(max_length=20, verbose_name='코드')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('price', models.IntegerField()),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='출고수량')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(verbose_name='출고가격')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='상품수량')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='입고수량')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(verbose_name='입고가격')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
        ),
    ]