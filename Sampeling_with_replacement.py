# Sampling a population with replacement.

# this script creates a bag of marbles of different colours.
# It then repeatedly samples the bag to build a statistical model of the bags contents
# the more times the bag is sampled and the larger the samples the closer the 
# more accurate are the predictions about the actual contents of the bag

#imports
import random
from collections import Counter

number_of_samples = 20
number_of_marbles_in_each_sample = 10

#######
#  Create the bag
#######


# set up the initial bag - we deicide how many of each colour to start with
number_of_each_colour_in_bag = {"white": 5000, "red": 2000}
# number_of_each_colour_in_bag = {"white": 5000, "red": 2000, "blue":500, "green":100, "yellow":50}
total_number_of_marbles_in_bag = sum(number_of_each_colour_in_bag.values())

#create a list object to be our empty bag
bag = [] 

# add the specified number of each colour marble to the bag.
for colour in number_of_each_colour_in_bag:
    for _ in range(1,number_of_each_colour_in_bag[colour]+1):
        bag.append(colour)

# we don't have to, but if you like you can shuffle the bag:
# random.shuffle(bag)

# we now have a bag of marbles 

#######
#  Sample the bag
#######

# initially we we know nothing about what is in the bag.
total_from_all_samples = {}

for sample_number in range(1,number_of_samples+1 ):
    # sample the bag and get number_of_marbles_in_each_sample marbles
    # we are not removing them from the bag - just recording a sample
    sample = random.sample(bag, number_of_marbles_in_each_sample)
    print("sample {}:".format(sample_number))

    marbles_in_this_sample = dict(Counter(sample))
    print(marbles_in_this_sample)
    # Add this information to our total_from_all_samples dictionary
    for colour in marbles_in_this_sample:
        if colour in total_from_all_samples:
            total_from_all_samples[colour] = total_from_all_samples[colour] + marbles_in_this_sample[colour]
        else:
            total_from_all_samples[colour] = marbles_in_this_sample[colour]
    print("the new total is now:")
    print (total_from_all_samples)
    print()

total_marbles_sampled = number_of_samples * number_of_marbles_in_each_sample
fraction_of_total_marbles_in_bag =  total_number_of_marbles_in_bag/total_marbles_sampled

# experimental probability
experimental_probability = {}
for item in total_from_all_samples:
    experimental_probability[item] = total_from_all_samples[item] * fraction_of_total_marbles_in_bag
 
print("How similar is each sample? are the samples big enough to be representative?")
print("------------------------------------------------------------------")
print("after {} samples of {} marbles from the bag  ".format(number_of_samples, number_of_marbles_in_each_sample))      
print("totalling {} marbles ".format(total_marbles_sampled))     
print("the final sample looks like: {}".format(total_from_all_samples))
print("the experimental probability calculated from our samples is now: {}".format(experimental_probability))
print("How close is this to the original bag? : {}".format(number_of_each_colour_in_bag))

