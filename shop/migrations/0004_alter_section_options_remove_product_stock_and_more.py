# Generated by Django 4.2.4 on 2025-03-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_section_product_sections'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('name',), 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='section',
            name='description',
        ),
    ]
