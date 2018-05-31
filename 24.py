"""What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
import itertools


permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(permutations[999999])




