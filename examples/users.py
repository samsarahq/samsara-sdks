from __future__ import print_function
import sys
import samsara

try:
    token = sys.argv[1]
except IndexError as e:
    print('Please provide an access token. For example:')
    print('python {program} <access token>'.format(program=sys.argv[0]))
    sys.exit()

# Create an ApiClient
client = samsara.ApiClient(
    header_name='Authorization',
    header_value='Bearer {token}'.format(token=token))

# Create an instance of the API
api = samsara.DefaultApi(api_client=client)

# Get the available user roles
# By default, Samsara always provides:
# - a "Full Admin" role
# - a "Read-only Admin" role
# among other default roles
user_roles = {}
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_user_roles(after=cursor)
    for user_role in res.data:
        user_roles[user_role.name] = user_role.id
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page
print("Collected {len} user roles".format(len=len(user_roles)))

# Create an organizational user with the Full Admin role
new_user = samsara.CreateUserRequest(
    name="Sam Saurus",
    email="sam.saurus@email.com",
    auth_type="default",
    roles=[
        samsara.UserRoleAssignmentRequest(
            role_id=user_roles['Full Admin']
        )
    ]
)
# Call API
res = api.create_user(new_user)
new_user_id = res.data.id
print("Created new user:")
print(res.data)

# Create a tag
new_tag = samsara.CreateTagRequest(
    name="Sam's Tag"
)
# Call API
res = api.create_tag(new_tag)
new_tag_id = res.data.id
print("Created {name}".format(name=res.data.name))

# Update the user to only have access to the tag
user_updates = samsara.UpdateUserRequest(
    roles=[
        samsara.UserRoleAssignmentRequest(
            role_id=user_roles['Full Admin'],
            tag_id=new_tag_id
        )
    ]
)
# Call the API
res = api.update_user(new_user_id, user_updates)
print("Updated user:")
print(res.data)

# Update user again to assign Read-only Admin
# at organizational level, and Full-Admin at tag level
user_updates = samsara.UpdateUserRequest(
    roles=[
        samsara.UserRoleAssignmentRequest(
            role_id=user_roles['Read-only Admin']
        ),
        samsara.UserRoleAssignmentRequest(
            role_id=user_roles['Full Admin'],
            tag_id=new_tag_id
        )
    ]
)
# Call the API
res = api.update_user(new_user_id, user_updates)
print("Updated user:")
print(res.data)

# Get the user
res = api.get_user(new_user_id)
print("User:")
print(res.data)

# List all users
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_users(after=cursor)
    for user in res.data:
        print("""
            {name}
            {email}
                Roles:
        """.format(name=user.name, email=user.email))
        for role_assignment in user.roles:
            print("""
                    {tag}
                    {role}
            """.format(
                role=role_assignment.role.name,
                tag=getattr(role_assignment.tag, 'name', 'Organization')))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Delete User and Tag
res = api.delete_user(new_user_id)
if res is None:
    print("Deleted user")
res = api.delete_tag(new_tag_id)
if res is None:
    print("Deleted tag")
