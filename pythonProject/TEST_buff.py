# coding=utf-8
from new_data import tutorial_pb2
from new_data import tutorial_info_pb2

address_book = tutorial_pb2.AddressBook()
person = address_book.people.add()

person.name = 'name1'
person.id = 12
person.email = 'name@gmail.com'

phones = person.phones.add()
phones.number = '1335555999'
phones.type = tutorial_info_pb2.PhoneType.MOBILE

phones = person.phones.add()
phones.number = '1335555991'
phones.type = tutorial_info_pb2.PhoneType.WORK

serialize_to_string = address_book.SerializeToString()

#写文件
import os
out_dir = "./"
with open(os.path.join(out_dir, "person.pb"), "wb") as f:
    f.write(address_book.SerializeToString())

def readpb():
    with open(os.path.join(out_dir, "person.pb"), "rb") as f:
        read_metric = tutorial_pb2.AddressBook()
        read_metric.ParseFromString(f.read())
        print('read_metric')
        print(read_metric.people)
        for person in read_metric.people:
            print(person)
            print("p_id：{},p_name：{},p_email：{}"
                  .format(person.id, person.name, person.email))
            for phone_number in person.phones:
                print(phone_number.number, phone_number.type)

readpb()
