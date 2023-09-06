# -*- coding: utf-8 -*-
"""못하나로관통할수있는막대의최대개수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Kya_8KZdYUOO44UR1II-dcUM5EmurxD
"""

n = int(input())

dict_s, dict_f = {}, {}
for i in range(n):
	a, b = map(int, input().split())
	dict_s[a] = dict_s.get(a, 0) + 1
	dict_f[b] = dict_f.get(b, 0) + 1

set_total = set(dict_s.keys()) | set(dict_f.keys())
total = list(set_total)
total.sort()

stick = 0
max_sum = 0
for j in range(len(total)):
	if total[j] in dict_s:
		stick += dict_s[total[j]]
	if j != 0 and	total[j-1] in dict_f:
			stick -= dict_f[total[j-1]]
	if max_sum < stick:
		max_sum = stick

print(max_sum)

#알고리즘 설명
#입력받은 구간 중 시작(start)부분과 끝(finish)부분으로 나누어 각각 dict_s와 dict_f에 key값과 key값의 개수를 value값으로 저장한다.
#그리고 각 딕셔너리의 key값을 set형태로 더해서 중복을 피한다.
#total list를 시작부터 끝까지 for문을 돌리면서 total의 key값이 dict_s에 존재한다면(못이 시작점을 만난다면) 그 value값(key값의 개수)를 stick에 더한다.
#total의 key값이 dict_f에 존재한다면(못이 끝점을 만난다면) 그 다음 key의 value값(key값의 개수)를 stick에서 뺀다.
#stick의 값 중 최대값을 구하여 출력한다.

#수행시간 분석
#가장 첫 for문이 돌아가는데 O(n).
#total 리스트를 sort하는데 최악의 경우 O(nlogn).
#-> set로 중복을 없애기 때문에 보통의 경우 nlogn보다 작다. 최악의 경우는 모든 구간의 시작과 끝이 한 개도 겹치지 않는 경우.
#두 번째 for문이 돌아가는데 최악의 경우 O(n).
#-> O(len(total))만큼의 시간이 걸리는데 중복이 없기 때문에 보통의 경우 len(total)이 n보다 작고, 최악의 경우 n이다.
#결국 최종 수행시간은 최악의 경우 O(n) + O(nlogn) + O(n) = O(nlogn)이다.