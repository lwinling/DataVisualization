# A program to calculate the area of visualization bubbles for HOLC article

import math

# Input the 1940 population for city 1

city_str_1 = input("Enter the name of the first city: ")

population_str_1 = input("Enter the 1940 census population of the first city: ")

population_int_1 = int(population_str_1)

# Input the 1940 population for city 2

city_str_2 = input("Enter the name of the second city: ")

population_str_2 = input("Enter the 1940 census population of the second city: ")

population_int_2 = int(population_str_2)

# Input the 1940 population for city 3

city_str_3 = input("Enter the name of the third city: ")

population_str_3 = input("Enter the 1940 census population of the third city: ")

population_int_3 = int(population_str_3)

# Ratio for city 1 based on approx Chicago population, which is a "unit circle" -- 1" radius

population_ratio_1 = population_int_1 / 3396808

# Calculate the area for city 1 using the ratio of the unit/Chicago circle

bubble_radius_1 = math.sqrt(population_ratio_1)

bubble_diameter_1 = (bubble_radius_1 * 2)

# Ratio for city 2 based on Chicago population, which is a "unit circle" -- 1" radius

population_ratio_2 = population_int_2 / 3396808

# Calculate the area for city 2 using the ratio of the unit/Chicago circle

bubble_radius_2 = math.sqrt(population_ratio_2)

bubble_diameter_2 = (bubble_radius_2 * 2)

# Ratio for city 3 based on Chicago population, which is a "unit circle" -- 1" radius

population_ratio_3 = population_int_3 / 3396808

# Calculate the area for city 3 using the ratio of the unit/Chicago circle

bubble_radius_3 = math.sqrt(population_ratio_3)

bubble_diameter_3 = (bubble_radius_3 * 2)

# List the calculation results

print("Population ratio (and bubble area ratio) of ", city_str_1, "versus Chicago is ", population_ratio_1)

print("Radius of the bubble is ", bubble_radius_1)

print("Diameter of the bubble is ", bubble_diameter_1)

print("Population ratio (and bubble area ratio) of ", city_str_2, "versus Chicago is ", population_ratio_2)

print("Radius of the bubble is ", bubble_radius_2)

print("Diameter of the bubble is ", bubble_diameter_2)

print("Population ratio (and bubble area ratio) of ", city_str_3, "versus Chicago is ", population_ratio_3)

print("Radius of the bubble is ", bubble_radius_3)

print("Diameter of the bubble is ", bubble_diameter_3)

