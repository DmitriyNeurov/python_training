__author__ = 'User'
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="", middlename=""))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Dmitriyppppp")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="", middlename=""))
#    app.contact.modify_first_contact(Contact(middlename="Dmitriy777"))
