#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import arena

urls = (
    '/player/(.*)', 'Player',
    '/', 'Index',
    '/fight/', 'Fight',
)


app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={ 'uid': 0 })
    web.config._session = session
else:
    session = web.config._session


class Player:
    def GET(self, name):
        if not name:
            name = 'Nobody'

        if not session.uid:
            p = arena.Player()

            session.uid = p.uid
            p.set_name(name)

        else:

            p = arena.Player(session.uid)

        return 'Hello, ' + p.name + '!' + str(p.uid)


class Index:
    def GET(self):
        return 'Hello,'



if __name__ == "__main__":
    app.run()

# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
