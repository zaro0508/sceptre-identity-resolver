# -*- coding: utf-8 -*-


from sceptre.resolvers import Resolver


class StackName(Resolver):
    """
    Resolves the the stack name.
    """

    def __init__(self, *args, **kwargs):
        super(StackName, self).__init__(*args, **kwargs)

    def resolve(self):
        return self.stack.external_name
