#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

print("Min # of operations to reach {} char: {}".format(0, minOperations(0)))
print("Min # of operations to reach {} char: {}".format(-1, minOperations(-1)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

