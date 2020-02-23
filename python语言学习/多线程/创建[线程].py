import threading
import time 

def func(cnt,name):
	for i in range(cnt):
		#time.sleep(2)
		print(" Hi {}".format(name))
		#time.sleep(2)
	#print(cnt," over")


def main():
	names = ['1_Rocky','2_Teny','3_lucy','4_Salary','5_Chen']
	for i in range(5):
		t = threading.Thread(target = func,args=(5,names[i]))
		#print(type(t))
		t.start()

if __name__ == '__main__':
	main()
