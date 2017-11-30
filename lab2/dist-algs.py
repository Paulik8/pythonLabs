ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 19,
    }, {
        "name": "petja",
        "age": 20,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 23,
    }, {
        "name": "petja",
        "age": 15,
    }],
}
K1Ll3aLl = {
    "name": "KiLR3@Ll",
    "age": 40,
    "children": [{
        "name":"jorik",
        "age": 19,
    }]
}
def info(emps, child_age=18):
    for emp in emps:
        for chd in emp['children']:
            if chd['age'] > child_age:
                print(emp['name'])
                break

emps = [ivan,darja,K1Ll3aLl]
info(emps)