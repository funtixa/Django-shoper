# Generated by Django 4.1.1 on 2022-09-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'waiting approval'), ('active', 'active'), ('deleted', 'deleted')], default='active', max_length=50),
        ),
    ]
