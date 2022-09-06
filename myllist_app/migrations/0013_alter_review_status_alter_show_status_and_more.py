# Generated by Django 4.0.6 on 2022-08-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0012_alter_showcharacter_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Plan', 'Plan'), ('Watching', 'Watching'), ('Completed', 'Completed')], default='none', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Upcoming', 'Upcoming'), ('Airing', 'Airing'), ('Finished Airing', 'Finished Airing')], default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='showcharacter',
            name='character_role',
            field=models.CharField(choices=[('None', 'None'), ('Supporting', 'Supporting'), ('Main', 'Main')], default='none', max_length=50),
        ),
    ]