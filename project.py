import csv

df = []
with open('final.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        df.append(row)

header = df[0]
planet_data_rows = df[1:]

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[4])
    planet_names.append(planet_data[1])
planet_gravity = []

for index, name in enumerate(planet_names):
    gravity = (float(planet_masses[index])*1.989e+30) /(float(planet_radiuses[index])*float(planet_radiuses[index])*6.957e+8*6.957e+8) * 6.674e-11
    planet_gravity.append(gravity)
