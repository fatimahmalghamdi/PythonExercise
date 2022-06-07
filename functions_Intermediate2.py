x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


def updateFunction(x):
    for i in range(0 , len(x)):
        # z = len(x[i])
        for j in range(0 , len(x[i])):
            if i == 1 and j == 0:
                x[i][j] = 15
    
    return x

print(updateFunction(x))





def changeName(students):
    # return students[0]["last_name"]
    for i in range(0 , len(students)):
        # print(len(students))
        mystr = students[i]['last_name'] 
        if mystr == "Jordan":
            students[i]['last_name'] = "Bryant"
    
    return students

print(changeName(students))
