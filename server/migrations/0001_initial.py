# Generated by Django 3.0.5 on 2020-04-13 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('g', 'Gramm'), ('kg', 'Kilogramm'), ('ml', 'Milliliter'), ('l', 'Liter'), ('tsp', 'Teaspoon'), ('tbs', 'Tablespoon'), ('box', 'Box'), ('can', 'Can'), ('pcs', 'Piece'), ('por', 'Portion')], max_length=3)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('emoji', models.CharField(max_length=3)),
                ('stock', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('picture', models.ImageField(upload_to='')),
                ('cooking_time', models.DurationField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(through='server.Ingredient', to='server.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Recipe'),
        ),
    ]
