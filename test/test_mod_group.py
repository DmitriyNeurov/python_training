__author__ = 'User'
import model.group

def test_modify_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group(model.group.Group(name="PDT - Py, group 3", header="Test automation1", footer="Each tester should be able to program :)))" ))
        app.session.logout()