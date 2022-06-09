# 라이브러리 불러오기
from tkinter import *

def click(key):
    print(key, "클릭했습니다.")

w = Tk()
w.title("간단한 계산기")

# 계산기 표시창
cal_win = Entry(w, width=33, bg='yellow')
cal_win.grid(row=0, column=0, columnspan=5)

# 버튼 4개 표시해보기
btn_list = ["AC", "+", "%", "/"]

row_num = 0
for b in btn_list:
    cmd = lambda x=b: click(x)
    btn = Button(w, text=b, width=5, 
                  relief='ridge', command=cmd)
    btn.grid(row=row_num//5+1, column=row_num%5)
    row_num += 1

w.mainloop()