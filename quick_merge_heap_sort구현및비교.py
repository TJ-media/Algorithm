# -*- coding: utf-8 -*-
"""Quick_Merge_Heap_Sort구현및비교.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gj50kvYkq3btkehqyU_Od_3nGk41-yu1
"""

import random, timeit
#quick sort
def quick_sort(A, first, last):
	global Qc, Qs
	if first >= last:
		Qc +=1
		return
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc += 1
		if left <=right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			Qs += 1
	A[first], A[right] = A[right], A[first]
	Qs +=1

	quick_sort(A, first, right - 1)
	quick_sort(A, right + 1, last)

#merge sort
def merge_sort(A, first, last):
	global Mc, Ms
	if first >= last: return
	merge_sort(A, first, (first+last) // 2)
	merge_sort(A, (first+last) // 2 + 1, last)
	merge_two(A, first, last)

def merge_two(A, first, last):
	global Mc, Ms
	m = (first + last) // 2
	i, j = first, m + 1
	B = []
	while i <= m and j <= last:
		if A[i] <= A[j]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
		Mc += 1
		Ms += 1
	for k in range(i, m + 1):
		B.append(A[k])
		Ms += 1
	for k in range(j, last + 1):
		B.append(A[k])
		Ms += 1
	for i in range(first, last + 1):
		A[i] = B[i - first]
		Ms += 1

#heap sort
def heap_sort(A):
	global Hc, Hs
	make_heap(A)
	n = len(A)
	for i in range(len(A) - 1, -1, -1):
		A[0], A[i] = A[i], A[0]
		Hs += 1
		n = n - 1
		heapify_down(A, 0, n)

def heapify_down(A, i, n):
	global Hc, Hs
	while i * 2 + 1 < n:
		L = i * 2 + 1
		R = i * 2 + 2
		if L < n and A[L] > A[i]:
			m = L
		else:
			m = i
		Hc += 1
		if R < n and A[R] > A[m]:
			m = R
			Hc += 1
		if m != i:
			A[i], A[m] = A[m], A[i]
			i = m
			Hs += 1
		else:
			break

def make_heap(A):
	global Hc,Hs
	n=len(A)
	for k in range(n-1, -1, -1):
		heapify_down(A,k,n)

######################################################################################
#insertion sort
def insertion_sort(A, first, last):
	global Qc, Qs
	for i in range(first + 1, last + n):
		j = i -1
		while j >= first and A[j] > A[j + 1]:
			A[j], A[j + 1] = A[j + 1], A[j]
			j = j - 1
			Qc += 1
			Qs += 1

def quick_sort1(A, first, last):
	global Qc, Qs
	if first >= last:
		Qc += 1
		return
	elif last - first <= 30:
		insertion_sort(A, first, last)
		return
	else:
		left, right = first + 1, last
		pivot = A[first]
		while left <= right:
			while left <= last and A[left] < pivot:
				left += 1
				Qc += 1
			while right > first and A[right] > pivot:
				right -= 1
				Qc += 1
			if left <= right:
				A[left], A[right] = A[right], A[left]
				left += 1
				right -= 1
				Qs += 1
		A[first], A[right] = A[right], A[first]
		Qs += 1

		quick_sort1(A,first, right - 1)
		quick_sort1(A, right + 1, last)

def quick_sort2(A, first, last):
	global Qc, Qs
	if first >= last:
		Qc += 1
		return
	elif last - first <= 30:
		return
	else:
		left, right = first + 1, last
		pivot = A[first]
		while left <= right:
			while left <= last and A[left] < pivot:
				left += 1
				Qc += 1
			while right > first and A[right] > pivot:
				right -= 1
				Qc += 1
			if left <= right:
				A[left], A[right] = A[right], A[left]
				left += 1
				right -= 1
				Qs += 1
		A[first], A[right] = A[right], A[first]
		Qs += 1

		quick_sort2(A,first, right - 1)
		quick_sort2(A, right + 1, last)
	insertion_sort(A, first, last)


def merge_sort3(A, first, last):
	if first >= last : return
	else:
		merge_sort3(A, first, first + (last - first) // 3)
		merge_sort3(A, first + (last - first) // 3, first + 2 * ((last - first) // 3) + 1)
		merge_sort3(A, first + 2 * ((last - first) // 3) + 1, last)
		merge_three(A, first, last)

def merge_three(A, first, last):
	global Mc, Ms
	m1 = first + (last - first) // 3
	m2 = first + 2 * ((last - first) // 3) + 1
	i, j, k, l = first, m1 + 1, m2 + 1, first
	B = []
	C = []
	while i <= m1 and j <= m2: #list A의 앞쪽 두 덩이 먼저 merge해서 list B에 저장
		if A[i] < A[j]:
			Mc += 1
			B.append(A[i])
			Ms += 1
			i += 1
		elif A[j] < A[i]:
			Mc += 1
			B.append(A[j])
			Ms += 1
			j += 1
	for k in range(i, m1 + 1):
		B.append(A[k])
		Ms += 1
	for k in range(j, m2 + 1):
		B.append(A[k])
		Ms += 1
	while l <= m2 and k <= last: #list B와 A의 남은 한덩이 merge해서 list C에 저장
		if B[l] < A[k]:
			Mc += 1
			C.append(B[l])
			Ms += 1
			l += 1
		elif A[k] < B[l]:
			Mc += 1
			C.append(A[k])
			Ms += 1
			k += 1
	for i in range(l, j):
		C.append(B[i])
		Ms += 1
	for i in range(k, last + 1):
		C.append(A[i])
		Ms += 1
	for i in range(first, last + 1):
		A[i] = C[i - first]
		Ms += 1


def tim_sort(A):
	A.sort()



def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))