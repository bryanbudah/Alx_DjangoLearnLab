# scripts/create_groups.py (run once with `python manage.py shell`)
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Book

# Define groups
groups_permissions = {
    "Editors": ["can_edit", "can_create"],
    "Viewers": ["can_view"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"]
}

content_type = ContentType.objects.get_for_model(Book)

for group_name, perms in groups_permissions.items():
    group, created = Group.objects.get_or_create(name=group_name)
    for perm_codename in perms:
        perm = Permission.objects.get(codename=perm_codename, content_type=content_type)
        group.permissions.add(perm)
