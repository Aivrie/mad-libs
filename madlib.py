adj = input("Please type in an adjective: ")
verb1 = input("Please type in a verb: ")
verb2 = input("Please type in another verb: ")
famous_person = input("Please type in a famous person: ")

madlib = "Computer programming is so {adj}, it makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}".format(adj=adj, verb1=verb1, verb2=verb2, famous_person=famous_person)

print(madlib)