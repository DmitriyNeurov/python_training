# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact( firstname="Dmitriy", middlename="Dmitriy1", lastname="Neurov", nickname="DmitriyNeurov", title="Software tester", company="Very best",
                            address="Russia, Moscow", home="+78955654", mobile="+74565456", work="+7456546456456", fax="+7454556",
                            email2="dmitriy.neurovdmitriy1.@best", email3="dmitriy.neurovdmitriy1.@best",
                            homepage="dmitriy.neurovdmitriy1.@best", byear="1986", address2="Russia, London", notes="gsgsgsfgssfgsfgs"))
        app.logout()

def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact( firstname="", middlename="", lastname="", nickname="", title="", company="",
                            address="", home="", mobile="", work="", fax="",
                            email2="", email3="",
                            homepage="", byear="", address2="", notes=""))
        app.logout()

