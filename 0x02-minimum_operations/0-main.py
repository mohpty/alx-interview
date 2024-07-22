#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

print("Min # of operations to reach {} char: {}".format(972, minOperations(972)))
print("Min # of operations to reach {} char: {}".format(27, minOperations(27)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

