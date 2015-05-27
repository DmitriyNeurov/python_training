__author__ = 'User'

def test_modification_first_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.modification_contact()
        app.session.logout()
