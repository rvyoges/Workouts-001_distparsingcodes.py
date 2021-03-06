#code Workouts

#Sort the list 
l1 = [3, 1, 4, 2, 5]
l1.sort()
print("The sorted list of l1 is")
print(l1)


#print the squares of all the number in the list 
l2 = [3, 1, 4, 2, 5]
newl2=[]
i=0
while(i<5):
  a=l2[i]
  a=a*a
  newl2.append(a)
  i=i+1
newl2.sort()
print("The squares of all the number in the list are")
print(newl2)


#print all the elements in the list 
l3 = [
    (105, "d"),
    (21, "z"),
    (0, "v")]
newl3=[]
i=0
while(i<3):
  newl3.extend(l3[i])
  i=i+1
print(newl3)


#Print all the value in the list
#print the hex value of green
#print the hex codes of all colors
l4 = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]
newl4=[]
i=0
while(i<3):
  newl4.extend(l4[i].values())
  i=i+1
print("The values in the list are")
print(newl4)
print("The hex value of green is")
print(l4[1]["value"])
print("The hex value of all colors are")
j=0
while(j<3):
  print(l4[j]["value"])
  j=j+1

#Print the languages that are inferior to Python
py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}
print(py["inferior"])

#Print my Bill
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
my_bill=my_purchase['apple']*prices['apple']+my_purchase['banana']*prices['banana']
print("Your bill is")
print(my_bill)

#print the items
#print the roles

junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}
newlist=[]
newlist.extend(junk["characters"]["Lonestar"]["items"])
newlist.extend(junk["characters"]["Barfolomew"]["items"])
newlist.extend(junk["characters"]["Dark Helmet"]["items"])
newlist.extend(junk["characters"]["Skroob"]["items"])
print("All the lists are")
print(newlist)
newrole=[]
newrole.append(junk["characters"]["Lonestar"]["role"])
newrole.append(junk["characters"]["Barfolomew"]["role"])
newrole.append(junk["characters"]["Dark Helmet"]["role"])
newrole.append(junk["characters"]["Skroob"]["role"])
print("All the Roles are")
print(newrole)

wtf = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}
#Get the first array value for the key 2
#Print all the array value for the key 2
#Print value of key 'a','b','c','d','e'
#Print the sum of the array with key 'e'
#set value of key 'e' to ['Chera','Chola','Pandiya']
print("The First array value for the key 2 is")
print(wtf[2][0])
print("All the array values for the key 2 are")
print(wtf[2])
print("value of key 'a','b','c','d','e' are")
print(wtf['a']['b']['c']['d']['e'])


x=len(wtf['a']['b']['c']['d']['e'])
i=0
sum=0
while(i<x):
  sum=sum+wtf['a']['b']['c']['d']['e'][i]
  i=i+1
print("the sum of the array with key 'e'")
print(sum)

print("set value of key 'e' ")
wtf['a']['b']['c']['d']['e']=['Chera','Chola','Pandiya']
print(wtf['a']['b']['c']['d']['e'])


#Get the value Mats from the Dict
body = {
    'query': {
        'filtered': {
            'query': {
                'match': {'description': 'addictive'}
            },
            'filter': {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}
print("Get the value Mats from the Dict")
#Modify the below statement to print Mats
#print(body["query"]['filtered']['filter'])
print(body["query"]["filtered"]["filter"]["term"].values())


# print the IMDB star rating ( 6.7)
# print the length of the movie

movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [ {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                   {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"} ]
    }
}
print("the IMDB star rating")
print(movie_box["Robin Hood: Men in Tights"]["imdb_stars"])
print("the length of the movie")
print(movie_box["Robin Hood: Men in Tights"]["length"])