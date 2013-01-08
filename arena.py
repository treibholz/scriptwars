#!/usr/bin/python
# -*- coding: utf-8 -*-

import web

db = web.database(dbn="sqlite", db="arena.db")

class Player(object): # {{{
    """docstring for Player"""
    def __init__(self, uid=False):
        super(Player, self).__init__()

        if not uid:
            self.uid = db.insert('Players')
            self.set_name('Nobody_%s' % self.uid)
        else:
            self.uid = uid

        player_load = db.select('Players', where = "uid = $self.uid", vars=locals())

        self.__dict__=  dict(player_load[0])


    def set_name(self, name):
        """docstring for set_name"""
        db.update('Players', name=name, where = "uid = $self.uid", vars=locals())

# }}}

# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
