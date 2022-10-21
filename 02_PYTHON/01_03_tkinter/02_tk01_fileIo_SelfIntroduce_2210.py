# tkinter
# 01. 자기 소개 내용 작성후, 파일로 작성 하는 함수 추가
# 02. 자기 소개 파일 내용 확인 함수 추가

from tkinter import *

window = Tk()
# window.geometry("350x200")  # 기본 창 사이즈 지정
window.title("자기 소개 나의 프로그램")

def click():
    print("클릭했어요.")

# 작성한 내용을 파일로 만들기
def make_content():
    print("자기소개 작성합니다.")
    doc = txt.get(1.0, END)  # 첫줄부터 마지막줄까지 얻어오기
    print("자기소개 내용 : ", doc)

    var = open("Self01.txt",'w',encoding = 'utf-8')

    if (doc != "") :
        var.write(doc)
        var.write("\n")
    var.close()

def fnc_quit():
    print("프로그램 종료")
    window.destroy()

# 01. 자기소개서 내용(레이블)
label1 = Label(window, text="자기소개 내용")
label1.pack()

# 02. 텍스트 박스 입력 상자
txt = Text(window, width=60, height=10, background='light green')
txt.pack()

# 03 자기 소개 작성
# grid(), pack()는 함께 사용할 수 없다.
# side => window의 widget의 일반적인 위치
btn1 = Button(window, text="자기소개 작성", width=20, command=make_content)
btn1.pack(side='left') #  'top', 'bottom', 'left', 'right' (default is 'top')

# 03 자기 소개 내용 확인
btn2 = Button(window, text="자기소개 확인", width=20, command=click)
btn2.pack(side='left')

# 03 프로그램 종료하기
btn3 = Button(window, text="프로그램 종료", width=20, command=fnc_quit)
btn3.pack()
window.mainloop()

# 실습. 자기소개 확인해 보기