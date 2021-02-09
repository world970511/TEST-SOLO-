import tkinter.filedialog as fd
from os.path import basename
import tkinter as tk
import os

def Load():
    filename = fd.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("csv files", "*.csv"),
                                          ("all files", "*.*")))

    work(filename)

def work(filename):
    f = open(filename, 'rt')
    hh_c = 0
    j_c = 0
    h_c = 0
    while True:
        line=f.readline().rstrip("\n")
        #readline()한줄씩 읽는 함수( read()=파일 전체/readlines()=파일 전체를 한줄씩 리스트의 원소로 담음)
        #rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거
        if line:
            line = line.split(",")#한줄씩 읽은 것을 ,를 기준으로 쪼갠다.
            hh_c += line.count("흑칠-흑진주패")
            j_c += line.count("주합칠-흑진주패")
            h_c += line.count("흑칠-진주패")
            #count()=리스트 안의 요소 개수를 반환하는 함수
        else:
            break
    cou(hh_c,h_c,j_c,filename)#카운트한 내용을 txt 파일에 저장하는 함수

def cou(hh_c,h_c,j_c,filename):
    f_2 = open('res.txt','at',encoding='utf-8')
    #res라는 텍스트 파일 오픈. utf-8로 인코딩
    #'a' =쓰기를 위해 열려 있고, 파일의 끝에 추가하는 경우 추가(파이썬 파일 사용시에 쓰는 모드)
    f_2.write("파일명: "+basename(filename)+"\n")
    #입력받은 경로의 기본 이름(base name)을 반환
    f_2.write("흑칠진주= "+str(h_c)+"\n")
    f_2.write("흑칠흑진주= "+str(hh_c)+"\n")
    f_2.write("주합칠= "+str(j_c)+"\n\n")

def Load_2():
    top.title(os.path.basename("./res.txt") + " - 메모장")
    ta.delete(1.0, tk.END)
    f=open("./res.txt","r",encoding="utf-8")
    ta.insert(1.0,f.read())
    f.close()

top = tk.Tk()
top.title("결과출력창")
top.geometry("300x300")

ta = tk.Text(top)
sb = tk.Scrollbar(ta)
sb.config(command = ta.yview)
sb.pack(side = tk.RIGHT, fill = tk.Y)
top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)
ta.grid(sticky = tk.N + tk.E + tk.S + tk.W) # ta 가 동서남북을 다 채우도록 고정

mb=tk.Menu(top)
fi = tk.Menu(mb, tearoff=0)
fi.add_command(label="파일찾기", command = Load)
fi.add_command(label="결과보기", command = Load_2)
fi.add_separator() #분리선 추가
mb.add_cascade(label="선택", menu=fi)# 파일 메뉴 메뉴바에 붙이기

top.config(menu=mb)
top.mainloop()