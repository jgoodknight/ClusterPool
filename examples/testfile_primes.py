# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:44:29 2015

@author: joseph
"""
import math
import random

import ClusterPool.ClusterPool as ClusterPool
import ClusterPool.Dispatcher as Dispatcher
import ClusterPool.PrimeChecker as PrimeChecker

number_of_primes_to_test = 61

number_range = (10**6, 10**10)
slow_Calculation_prime = 5915587277
numbers = []
objects_to_calculate = []

def RED_BUTTON(x):
    return x.calculate()

for i in range(number_of_primes_to_test):
    new_possibly_prime_number = random.randint(*number_range)
    # print("will check %i " % new_possibly_prime_number)
    objects_to_calculate.append(PrimeChecker.is_prime(new_possibly_prime_number))

objects_to_calculate.append(PrimeChecker.is_prime(slow_Calculation_prime))

initial_test_object = PrimeChecker.is_prime(858599503)

print "initiating Pool"
# myPool = ClusterPool.Pool(cluster_dispatcher_type = "SLURM", TEST_MODE=True)
myPool = ClusterPool.Pool(cluster_dispatcher_type = "normal", TEST_MODE=True)
print "mapping calculation onto object"
calculated_objects = myPool.map(RED_BUTTON, objects_to_calculate)
print "calculations done, reading results"
for i, obj in enumerate(calculated_objects):
    try:
        print i, obj.number_that_may_be_prime, obj.isPrime
    except:
        print("problem..., calculation spat this out: ", obj)
