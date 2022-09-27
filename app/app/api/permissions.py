# from rest_framework.permissions import BasePermission

# from company_portal.entitlements import is_organisation_manager


# class PermissionsByActionMixin:
#     """
#     Determine permissions based on priority, from higher to lower:

#     - permission_classes_by_action attribute

#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
#         'default': permission_classes, # (if not one of the previous)
#     }

#     """

#     def get_permissions(self):
#         """
#         Check all permissions strategies.
#         """
#         try:
#             permission_classes = self.permission_classes_by_action[self.action]
#         except KeyError:
#             try:
#                 permission_classes = self.permission_classes_by_action["default"]
#             except KeyError:
#                 raise Exception("Permissions for this action have not being specified.")

#         res = [permission() for permission in permission_classes]

#         return res


# class OrganisationManagersPermission(BasePermission):

#     def has_permission(self, request, view):
#         return is_organisation_manager(request.user)
