# 곱하기 계산
import tkinter as tk

def 계산하기( ):
	입력글1 = 입력1.get( )
	입력글2 = 입력2.get( )
	답 = int(입력글1) * int(입력글2)
	결과.config(text='결과: ' + str(답))

메인창 = tk.Tk()
메인창.title('계산기')

입력1 = tk.Entry(메인창, width=10)
입력1.pack(side=tk.LEFT)

연산자 = tk.Label(메인창, text='X')
연산자.pack(side=tk.LEFT)

입력2 = tk.Entry(메인창, width=10)
입력2.pack(side=tk.LEFT)

계산 = tk.Button(메인창, text='계산', command=계산하기)
계산.pack(side=tk.LEFT)

결과 = tk.Label(메인창, text='결과: ', width=20, anchor='w')
결과.pack(side=tk.LEFT)

메인창.mainloop()
