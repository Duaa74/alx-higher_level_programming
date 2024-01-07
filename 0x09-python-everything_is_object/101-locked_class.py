#!/usr/bin/python3
"""defined a locked class"""


class LockedClass:
    """
    prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
