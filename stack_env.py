# -*- coding: utf-8 -*-


from sceptre.resolvers import Resolver


class StackEnvironment(Resolver):
    """
    Resolves the stack configuration environment name
    """

    def __init__(self, *args, **kwargs):
        super(StackEnvironment, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the current date.

        :returns: the current date
        :rtype: str
        """
        env = self.stack.name.split('/')[0]
        return env
