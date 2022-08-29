budget = int(input("Mars budget: "))
project1 = int(input("Cost of project Cloud Seeding: "))
project2 = int(input("Cost of project Equatorial Magnetizer: "))
project3 = int(input("Cost of project Space Elevator: "))

if project1 + project2 + project3 <= budget:
    print("We have enough budget to initiate all projects.")
else:
    print("Some projects will have to wait.")