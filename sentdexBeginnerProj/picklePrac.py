exec("print('siho')")

list_str = "[4,3,2,4,3]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [5,3,4,5]")
print(list_str2)

exec("def test(): print('o snap')")
test()

exec("""
def test2():
    print('lets see if multi owrks')

""")

test2()