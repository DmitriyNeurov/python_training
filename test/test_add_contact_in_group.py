from model.group import Group
from model.contact import Contact


def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="Dmitriy"))
    old_contacts = db.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    old_contacts_in_group = orm.get_contacts_in_group(Group(id="2"))
    app.contact.add_contact_in_group()
    new_contacts_in_group = orm.get_contacts_in_group(Group(id="2"))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)

