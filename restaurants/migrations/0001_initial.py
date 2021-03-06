# Generated by Django 4.0.4 on 2022-05-02 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('group_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.group')),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['group_name'], name='group_name_idx'),
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['restaurant_name'], name='restaurant_name_idx'),
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['city'], name='city_idx'),
        ),
    ]
