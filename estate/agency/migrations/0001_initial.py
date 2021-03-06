# Generated by Django 2.2.5 on 2019-10-16 15:40

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('contenue', tinymce.models.HTMLField(verbose_name='contenue')),
                ('prix', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('image_accueil', models.ImageField(blank=True, upload_to='img')),
                ('isDisponible', models.BooleanField(default=False)),
                ('isSoldout', models.BooleanField(default=False)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_house', to='blog.Category')),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('image_vue', models.ImageField(blank=True, upload_to='img')),
                ('lien_video', models.CharField(blank=True, max_length=255)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_location', to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Info_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('noumbre', models.CharField(max_length=255)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_info', to='agency.House')),
            ],
        ),
        migrations.CreateModel(
            name='image_apercu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_apercu', to='agency.House')),
            ],
        ),
    ]
