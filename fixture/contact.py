__author__ = 'User'
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" %id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def modify_first_contact(self):
        wd=self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_date):
        # open modification form
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(new_contact_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def modify_contact_by_id(self, id, new_contact_date):
        # open modification form
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(new_contact_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash=None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cash.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                 address=address, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))

        return list(self.contact_cash)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        address, email, email2, email3, firstname, home, id, lastname, mobile, phone2, work = self.get_element_value(wd)
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email,
                       email2=email2, email3=email3, home=home, mobile=mobile, work=work, phone2=phone2)

    def get_element_value(self, wd):
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return address, email, email2, email3, firstname, home, id, lastname, mobile, phone2, work

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

   #     wd = self.app.wd
   #     self.open_contact_view_by_index(index)
   #     text = wd.find_element_by_id("content").text
   #     home = re.search("H: (.*)", text).group(1)
   #     work = re.search("W: (.*)", text).group(1)
   #     mobile = re.search("M: (.*)", text).group(1)
   #     phone2 = re.search("P: (.*)", text).group(1)
   #     return Contact(home=home, mobile=mobile, work=work, phone2=phone2)









