# Generated by Django 4.2.1 on 2023-06-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipesingredients_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='name',
            field=models.CharField(help_text='Название ингредиента', max_length=256, verbose_name='Название ингредиента'),
        ),
    ]