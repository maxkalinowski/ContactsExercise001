# read contacts.json and print the names of the contacts
import json
import xml.etree.ElementTree as ET


def readContacts():
    with open('contacts.json') as f:
        contacts = json.load(f)
        print(contacts)
    return contacts

# write a function to write contacts to an XML file


def writeContactsToXML(contactList):
    # create a new XML file and open it for writing
    data = ET.Element('data')
    contacts = ET.SubElement(data, 'contacts')

    # create subelements with the contact information
    for contact in contactList:
        item = ET.SubElement(contacts, 'item')
        name = ET.SubElement(item, 'name')
        name.text = contact['name']
        email = ET.SubElement(item, 'email')
        email.text = contact['email']

    # create a new XML file with the results
    mydata = ET.tostring(data)
    myfile = open("contacts.xml", "wb")
    myfile.write(mydata)

# write a fuction to write contacts dictionary with array of name, email to a CSV file


def writeContactsToCSV(contactList):
    # open a new file for writing
    f = open("contacts.csv", "w")
    # create the column headings
    f.write("name,email \n")
    # write a row for each contact
    for contact in contactList:
        f.write(contact['name'] + "," + contact['email'] + "  \n")

    # close the file
    f.close()


contacts = readContacts()

writeContactsToXML(contacts["contacts"])
writeContactsToCSV(contacts["contacts"])
