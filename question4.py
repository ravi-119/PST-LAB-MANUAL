a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter b : "))

# calculate discriminent
discriminent = b**2 - 4*a*c

if discriminent >= 0:
    root1 = (-b + (discriminent ** 0.5))/ (2*a)
    root2 = (-b - (discriminent ** 0.5))/ (2*a)
    print("root1 is => ",int(root1))
    print("root2 is => ",int(root2))
else:
    print("The value of discriminent is negative")






# # Get coefficients a, b, and c from the user
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# # Calculate the discriminant
# discriminant = b**2 - 4*a*c

# # Check if the discriminant is non-negative
# if discriminant >= 0:
#     # Calculate the roots
#     root1 = (-b + (discriminant ** 0.5)) / (2 * a)
#     root2 = (-b - (discriminant ** 0.5)) / (2 * a)

#     print(f"The roots of the quadratic equation are: {root1} and {root2}")
# else:
#     print("The quadratic equation has complex roots.")