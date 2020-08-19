from __future__ import unicode_literals

from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    d3_js_permissions = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                              content_type__model='d3_js')

    react_js_permissions = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                                 content_type__model='react_js')

    d3_react_js_permissions = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                        content_type__model='d3_react_js')

    perm_view_d3_js = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                            content_type__model='d3_js',
                                                            codename='view_d3_js')

    perm_view_react_js = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                               content_type__model='react_js',
                                                               codename='view_react_js')

    perm_view_d3_react_js = permission_class.objects.filter(content_type__app_label='dsrs_viz',
                                                      content_type__model='d3_react_js',
                                                            codename='view_d3_react_js'
                                                            )


    power_permissions = chain(d3_js_permissions,
                              react_js_permissions,
                              d3_react_js_permissions)


    editor_permissions = chain(d3_js_permissions,
                               react_js_permissions,
                               d3_react_js_permissions)


    viewer_permissions = chain(perm_view_d3_js,
                                       perm_view_react_js,
                                       perm_view_d3_react_js)


    my_groups_initialization_list = [
        {
            "name": "power",
            "permissions_list": power_permissions,
        },
        {
            "name": "editor",
            "permissions_list": editor_permissions,
        },
        {
            "name": "viewer",
            "permissions_list": viewer_permissions,
        },

    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('dsrs_viz', '0003_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
