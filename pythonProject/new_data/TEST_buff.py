# coding=utf-8
#import people_pb2
import  tutorial_pb2
import  tutorial_info_pb2
import random

address_book = tutorial_pb2.AddressBook()
person = address_book.people.add()

person.name='name1'
person.id=12
person.email='name@gmail.com'

phones = person.phones.add()
phones.number='1335555999'
phones.type = tutorial_info_pb2.PhoneType.MOBILE

phones = person.phones.add()
phones.number='1335555991'
phones.type = tutorial_info_pb2.PhoneType.WORK

serialize_to_string = address_book.SerializeToString()
print(serialize_to_string, type(serialize_to_string))

#反序列化
address_book.ParseFromString(serialize_to_string)
for person in address_book.people:
    #print(person)
    print("p_id：{},p_name：{},p_email：{}"
          .format(person.id, person.name, person.email))

    for phone_number in person.phones:
        print(phone_number.number, phone_number.type)

#写文件
import os
out_dir = "./"
with open(os.path.join(out_dir, "person.pb"), "wb") as f:
    # binary output
    f.write(address_book.SerializeToString())
with open(os.path.join(out_dir, "person.protobuf"), "w") as f:
    f.write(str(address_book))

def readpb():
    with open(os.path.join(out_dir, "person.protobuf"), "rb") as f:
        r_buff = f.read()
        print(r_buff)
        read_metric = people_pb2.AddressBook()
        print(type(r_buff))
        read_metric.ParseFromString(r_buff)
        for person in read_metric.people:
            print("p_id：{},p_name：{},p_email：{}"
                  .format(person.id, person.name, person.email))
            for phone_number in person.phones:
                print(phone_number.number, phone_number.type)

readpb()