file = open("teams.txt", "w")

file.writelines(["Man United", "\nChelsea", "\nArsenal", "\nLiverpool", "\nBarcelona" ])
file.close()

file = open("teams.txt", "r")

lines = file.readlines()

print(lines[0].strip())
print(lines[3].strip())

file.close()