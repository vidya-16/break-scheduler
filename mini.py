import webbrowser
import time


n=float(input(" after how many hours  you need a break?  "))
m=float(input("specify no. of times you need a break :  "))
i=0
j=0
while( i<m):
	
	if j==n:
		
		print("break")
		webbrowser.open("www.amazon.com",2)
		time.sleep(60)  //60 secs break
		j=0
		i=i+1
	else:
		print("time to work!")
		j=j+1
