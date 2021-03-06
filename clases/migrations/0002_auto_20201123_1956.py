# Generated by Django 2.2.14 on 2020-11-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('edad', models.IntegerField(null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('activo', models.BooleanField(null=True)),
                ('clases', models.ManyToManyField(related_name='estudiantes', to='clases.Clase')),
            ],
        ),
    ]
