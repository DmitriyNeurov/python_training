__author__ = 'User'
from model.contact import Contact

def test_modify_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_contact(Contact (firstname="Dmitriy123", middlename="Dmitriy111", lastname="Neurov213", nickname="DmitriyNeurov3", title="Software tester!", company="Very best!",
                            address="Russia, Moscow!", home="+7895565412", mobile="+7456545612", work="+7456546456456123", fax="+745455613",
                            email2="dmitriy.neurovdmitriy123.@best", email3="dmitriy.neurovdmitriy123.@best",
                            homepage="dmitriy.neurovdmitriy123.@best", byear="1988", address2="Russia, London!", notes="aaaa" ))
        app.session.logout()
