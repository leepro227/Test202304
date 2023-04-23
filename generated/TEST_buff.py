# coding=utf-8
# 运行环境为linux,运行结果图见：TEST_buff_run.png
import person_pb2
import person_info_pb2

address_book = person_pb2.AddressBook()
person = address_book.people.add()

person.name='name1'
person.id=12
person.email='name@gmail.com'

phones = person.phones.add()
phones.number='1335555999'
phones.type = person_info_pb2.PhoneType.MOBILE

phones = person.phones.add()
phones.number='1335555991'
phones.type = person_info_pb2.PhoneType.WORK

serialize_to_string = address_book.SerializeToString()
print(serialize_to_string, type(serialize_to_string))

address_book.ParseFromString(serialize_to_string)
for person in address_book.people:
    #print(person)
    print("p_id：{},p_name：{},p_email：{}"
          .format(person.id, person.name, person.email))

    for phone_number in person.phones:
        print(phone_number.number, phone_number.type)