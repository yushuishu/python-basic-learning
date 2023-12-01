"""
字符串相关操作
"""
string = "hello world python java golang"
print(string[1])
print(string[-1])
print(string.index("el"))
replace_string = string.replace(" ", "_")
print(f"原字符串：{string}，替换后的字符串：{replace_string}")
split_string = string.split(" ")
print(f"{split_string}， 类型: {type(split_string)}")
string2 = "   aaa 123456789 bbb "
print("去除前尾空格", string2.strip())
string3 = "aaa 12345aaa6789 bbbaaa"
print("去除前尾指定字符", string3.strip("aaa"))
print("统计字符", string3.count("aaa"))
print("长度", len(string3))

