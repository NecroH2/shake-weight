# Generated by Django 2.1.2 on 2018-10-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_perro_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='estado',
            field=models.CharField(choices=[(1, 'Disponible'), (2, 'Rescatado'), (3, 'Adoptado')], default='Rescatado', max_length=20),
        ),
    ]
