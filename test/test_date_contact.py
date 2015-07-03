import re
from random import randrange
from model.contact import Contact

def test_date_on_home_page(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="Dmitriy"))
    old_contacts = db.get_contact_list()
    randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))