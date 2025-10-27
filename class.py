#string1 ="hello"
#print(string1.capitalize())
#print(string1)

#Wont change string1 because strings are immutable
#string1 = string1.capitalize()
#print(string1)
#Will change string1 because we reassigned it to the capitalized version of itself
#print(string1)

#new examople
# player_details_list={ "name": "john", "age":  25, "height": 6.5, "profession": "Basketball"}

# print(player_details_list["name"])
# print(player_details_list["age"])       
# print(player_details_list["height"])
# print(player_details_list["profession"])
# ordering ={
#     1:"one",
#     2:"two"
# }
# print(ordering[1])

"""mixed_dict={
    True:"bool key",
    False:"bool value"
}
print(mixed_dict[True])"""








print("hello user")
price=int(input("Enter price: "))
if price < 1000:
    price=price*95/100
    print("Price is less than 1000")
elif price >=1000 and price <5000:
    price=price*90/100
    print("Price is between 1000 and 5000")
elif price >=5000:
    price=price*75/100
    print("Price is greater than or equal to 5000")

print("the current price is:", price)
age=int(input("Enter your age: "))
if age < 70:
    price=price*95/100
    print("Age is more than 70")
else:
    print("no discount available")
print("the current price is:", price)
membership=input("Are you a member? (yes/no): ")
if membership.lower() == "yes":
    price=price*95/100
    print("Member discount applied")
print("the final price is:", price)

































