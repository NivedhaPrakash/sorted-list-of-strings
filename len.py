def func():
	s=raw_input()
	i=s.split()
	print(sorted(i,key=len))