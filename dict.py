dict_this= {
        "brand":"samsung",
        "processor":"8Gen3",
        "ram":"12GB",
        "ram":"16GB",
        "ssd":"256GB"
        }
print(dict_this)
print(type(dict_this))



one_p= dict(brand="one-plus",processor="8Gen1",Ram="12GB",ssd="256GB")
print(one_p)
print(type(one_p))



jay= {
        "name":"jay",
        "surname":"adhar",
        "roll":1,
        "dob":"8th july"
        }

jay["name"]="jayanth"
print(jay)

z=jay.get("roll")
print(z)
x=jay.keys()
print(x)
c=dict_this.items()
print(c)
y=jay.values()
print(y)



vara= {
        "name":"vara",
        "company":"AMD",
        "ID":"5471"
        }

del vara    
print(vara)


h=jay.copy()
print(h)
