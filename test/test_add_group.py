# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="PDT - Py, group 2", header="Test automation", footer="Each tester should be able to program :)"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()


