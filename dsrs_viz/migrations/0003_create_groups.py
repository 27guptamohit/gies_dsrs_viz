from django.db import migrations

GROUPS = [
    {
        'name': 'viewer',
    },
    {
        'name': 'editor',
    },
    {
        'name': 'power',
    },

]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('dsrs_viz', '0002_auto_20200819_0035'),
    ]

    operations = [

        migrations.RunPython(
            add_group_data,
            remove_group_data
        )

    ]
