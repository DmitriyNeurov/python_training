# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="Dmitriy", middlename="Dmitriy1", lastname="Neurov", nickname="DmitriyNeurov", title="Software tester", company="Very best",
                            address="Russia, Moscow", home="+78955654", mobile="+74565456", work="+7456546456456", fax="+7454556",
                            email2="dmitriy.neurovdmitriy1.@best", email3="dmitriy.neurovdmitriy1.@best",
                            homepage="dmitriy.neurovdmitriy1.@best", byear="1986", address2="Russia, London", phone2="+7895325525", notes="gsgsgsfgssfgsfgs")
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




#def test_add_empty(app):
 #       old_contacts = app.contact.get_contact_list()
  #      contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
   #                         address="", home="", mobile="", work="", fax="",
    #                        email2="", email3="",
     #                       homepage="", byear="", address2="", phone2="", notes="")
      #  app.contact.create(contact)
       # new_contacts = app.contact.get_contact_list()
        #assert len(old_contacts) + 1 == len(new_contacts)
        #old_contacts.append(contact)
        #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

