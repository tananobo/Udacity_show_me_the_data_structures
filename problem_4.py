class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

other = Group("other")

from collections import deque

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    d = deque()
    d.append(group)
    while d:
        group = d.popleft()
        if user in group.users:
            return True
        for i_group in group.groups:
            d.append(i_group)

    return False

#TEST 1
print(is_user_in_group("sub_child_user", parent))

#TEST 2
print(is_user_in_group("sub_child_user", child))

#TEST 3
print(is_user_in_group("sub_child_user", sub_child))

#TEST 4
print(is_user_in_group("sub_child_user", other))

#TEST 5
print(is_user_in_group("", other))