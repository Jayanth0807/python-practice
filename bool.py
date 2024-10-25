x="hello"
y=77

print(bool(x))
print(bool(y))


class my_class():
    def __len__(self):
        return 0

obj=my_class
print(bool(obj))


z=235

print(isinstance(z,float))
