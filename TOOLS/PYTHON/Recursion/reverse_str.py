# def reverse_str(data):
#
#     if not data:
#         # връща същия празен стринг
#         return data
#
#     return reverse_str(data[1:]) + data[0]
#
# print(reverse_str("123456"))



def reverse_s(string):
    if string == "":
        return ""

    get_num = string[0]
    result = string[1:]
    return reverse_s(result) + get_num

    # върни стр[0](1) + нещо
    # нещото == стр[0](2) + нещо
    # нещото == стр[0](3) + нещо
    # нещото == стр[0](4) + нещо
    # нещото == стр[0](5) + нещо
    # нещото е == ""

print(reverse_s("12345"))