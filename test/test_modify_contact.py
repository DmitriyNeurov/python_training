__author__ = 'User'
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename=""))
    app.contact.modify_first_contact(Contact(firstname="Dmitriyppppp"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename=""))
    app.contact.modify_first_contact(Contact(middlename="Dmitriy777"))
