# Generated by Django 2.0.2 on 2018-03-19 07:28

from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteRole',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('permissions', multiselectfield.db.fields.MultiSelectField(choices=[('AddB', 'Add Body'), ('DelB', 'Delete Body'), ('BodyChild', 'Modify Body-Child Relations'), ('Location', 'Full control over locations'), ('Role', 'Modify Institute Roles')], max_length=33)),
            ],
            options={
                'verbose_name': 'Institute Role',
                'verbose_name_plural': 'Institute Roles',
            },
        ),
        migrations.AlterModelOptions(
            name='bodyrole',
            options={'verbose_name': 'Body Role', 'verbose_name_plural': 'Body Roles'},
        ),
        migrations.AlterField(
            model_name='bodyrole',
            name='permissions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles')], max_length=24),
        ),
    ]