# models flipping two coins X number of times and counts the number
# of double heads
import random

number_of_flips = 150
number_of_two_heads = 0

def flip_two_coins():
    return (random.choice(["Heads","Tails"]), random.choice(["Heads","Tails"]))

for i in range(0,number_of_flips):
    flip = flip_two_coins()
    if flip == ("Heads", "Heads"):
        number_of_two_heads += 1
   
   
    
print(".....")
print("Double 'Heads' was thrown {} times in  {} flips: P(double heads) = {}".format(number_of_two_heads,number_of_flips, number_of_two_heads/number_of_flips))
