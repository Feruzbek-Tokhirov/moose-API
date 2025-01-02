# Generated by Django 5.1.4 on 2025-01-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=202)),
                ('image', models.ImageField(upload_to='about/')),
                ('body', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('how_i_work', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
