#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Borg:
    __shared_state = {}

    def __init__(self, value):
        self.__dict__ = self.__shared_state
        self.state = value

    def __str__(self):
        return self.state


class DerivedBorg(Borg):
    pass

