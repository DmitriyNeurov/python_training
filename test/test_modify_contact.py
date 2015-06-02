__author__ = 'User'
from model.contact import Contact

def test_modify_contact_firstname(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_first_contact(Contact(firstname="Dmitriyppppp"))
        app.session.logout()

def test_modify_contact_middlename(app):
      app.session.login(username="admin", password="secret")
      app.contact.modify_first_contact(Contact(middlename="Dmitriy777"))
      app.session.logout()
