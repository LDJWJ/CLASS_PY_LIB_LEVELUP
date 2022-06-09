# 라이브러리 불러오기
from tkinter import *

def click(key):
    print(key, "클릭했습니다.")
    if key == "=":
        try:
            result = eval( cal_win.get() )
            cal_win.delete(0, END)
            cal_win.insert( END, str(result) )
        except:
            cal_win.insert(END, "ERROR!!!")
    elif key=="AC":
        cal_win.delete(0, END)
    else:
        cal_win.insert( END, key )

w = Tk()
w.title("간단한 계산기")

# 계산기 표시창
cal_win = Entry(w, width=25, bg='yellow', font=("MS Sans Serif 20"))
cal_win.grid(row=0, column=0, columnspan=4, sticky="e")

# 버튼 4개 표시해보기
btn_list = ["AC", "+", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "^", "="]

row_num = 0
for b in btn_list:
    cmd = lambda x=b: click(x)

    # relief : 3차원 효과
    btn = Button(w, text=b, width=5, 
                  relief='ridge', command=cmd)
    
    # 4개 버튼이 차면 다음 줄로 이동
    btn.grid(row=row_num//4+1, column=row_num%4)
    row_num += 1

w.mainloop()

# (간단 생각해보기)
# button을 한 행에 4개가 아닌 5개를 넣어보자.
# ^ 연산자 계산 기능 추가

# REF
# https://realpython.com/python-gui-tkinter/
# Font List : https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter