import csv
import pandas as pd

df = pd.read_csv('final.csv')
df.drop(['Unnamed: 0'],axis=1,inplace=True)
# print(df.head())
# print(df.shape)
# print(df.dtypes)

radius = df['radius'].to_list()
mass = df['mass'].to_list()
gravity =[]

for i in range(0,len(radius)):
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g = (mass[index]*G)/((radius[index])**2)
        gravity.append(g)

gravity_calculation(radius,mass)
df["gravity"] = gravity
# print(df.head())
df.to_csv('data.csv')