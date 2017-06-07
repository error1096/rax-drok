from Tkinter import *
import ttk,os

root = Tk()
root.resizable(0,0)
root.iconbitmap('py.ico')
root.title("private DROK generator BY[error1096]")
s = ttk.Style()
s.theme_names()
s.theme_use('clam')


def error1096():  # error1096 DEF

    error1096_TK = Tk()
    error1096_TK.title("error1096")

    # just simpel label simpel

    Label(error1096_TK, text="""hello \n my name is error1096 \n and im a simpel \n programmer 
if you nead any help contact \n me you can find my email address in \n contact menu """).pack()

    Label(error1096_TK, text="""

                 hello                                                
                   my name                                         
                     is error1096                                      
                      and im a simpel                                     
                        programmer                                    
                        if                                     
                        you nead                                   
                         any help                                  
                           contact                                 
                             me you                                
                              can find                              
                               my email                           
                                address in                           

""").pack()

    error1096_TK.mainloop()


def contactME():  # contact DEF

    contactME_TK = Tk()

    contactME_TK.title("contact")

    # just simpel label simpel

    Label(contactME_TK, text="my GMAIL :", fg='red').grid(row=0, column=0)
    Label(contactME_TK, text="assasin.shahin@gmail.com", fg='blue').grid(row=0, column=1)

    Label(contactME_TK, text="GIThub :", fg='red').grid(row=1, column=0)
    Label(contactME_TK, text="https://github.com/error1096", fg='blue').grid(row=1, column=1)

    Label(contactME_TK, text="tw&instagram :", fg='red').grid(row=2, column=0)
    Label(contactME_TK, text="error1096", fg='blue').grid(row=2, column=1)


menu =  Menu(root)#menu
root.config(menu=menu)

s1MENU =  Menu(menu)#sube menu (about menu)
menu.add_cascade(label="ABOUT ME" , menu=s1MENU)
s1MENU.add_command(label="ERRO1096",command=error1096)#sube menu 1
s1MENU.add_command(label="CONTACT ME.",command=contactME)#sube menu 2

# ~BOX1 !
BOX1 = ttk.LabelFrame(root,text='part1')

S = ttk.Scrollbar(BOX1)

textBOXn0 = Text(BOX1,height=15,width=25)

S.pack(side=LEFT,fill=Y)

textBOXn0.pack()

S.config(command=textBOXn0.yview)

textBOXn0.config(yscrollcommand=S.set)

BOX1.grid(row=0,column=0)

# ~BOX2 !

BOX2 = ttk.LabelFrame(root,text='part2')

S = ttk.Scrollbar(BOX2)

textBOXn1 = Text(BOX2,height=15,width=25)

S.pack(side=LEFT,fill=Y)

textBOXn1.pack()

S.config(command=textBOXn0.yview)

textBOXn1.config(yscrollcommand=S.set)

textBOXn1.insert(END,""".php?
.aspx?
.asp?
.cfm?
.html?
.cgi?""")

BOX2.grid(row=0,column=1)
# ~BOX3 !
BOX3 = ttk.LabelFrame(root,text='part3')
S = ttk.Scrollbar(BOX3)
textBOXn2 = Text(BOX3,height=15,width=25)
S.pack(side=LEFT,fill=Y)

textBOXn2.pack()

S.config(command=textBOXn0.yview)

textBOXn2.config(yscrollcommand=S.set)

BOX3.grid(row=0,column=2)
textBOXn2.insert(END,"""jobid=
item_id=
id=
topic=
NewsId=
newsid=
langid=
article_id=
""")
# ~BOX4 !
BOX4 = ttk.LabelFrame(root,text='part4')
S = ttk.Scrollbar(BOX4)

textBOXn3 = Text(BOX4,height=10,width=80)
lin = textBOXn0.get("1.0",END)
S.pack(side=LEFT,fill=Y)

textBOXn3.pack()

S.config(command=textBOXn0.yview)

textBOXn3.config(yscrollcommand=S.set)

BOX4.grid(row=1,columnspan=3)




def test():
    Z = textBOXn0.get("1.0", END)
    X = textBOXn1.get("1.0", END)
    C = textBOXn2.get("1.0", END)
    V = textBOXn3.get("1.0", END)

    with open("date1.txt", 'w') as q:

        with open("date2.txt", 'w') as w:

            with open("date3.txt", 'w') as e:

                with open("date4.txt", 'w') as r:

                    q.write(Z)
                    w.write(X)
                    e.write(C)
                    r.write(V)

    with open("date1.txt", 'r') as A:

        with open("date2.txt", 'r') as S:

            with open("date3.txt", 'r') as D:

                with open("date4.txt", 'r') as F:

                    with open('GOLDEdrok_by_error1096.txt','w') as o :


                        a = A.read().split("\n")
                        s = S.read().split("\n")
                        d = D.read().split("\n")
                        f = F.read().split("\n")

                        for line_a in a:
                            for line_s in s:
                                for line_d in d:
                                    for line_f in f:

                                        if not sit.get():

                                            part1 = str(line_a)
                                            part2 = str(line_s)
                                            part3 = str(line_d)
                                            part4 = str(line_f)
                                            newline = "\n"
                                            o.write(part1+part2+part3+part4+newline)

                                        else:
                                            inurl = " site:"+str(sit.get())
                                            part1 = str(line_a)
                                            part2 = str(line_s)
                                            part3 = str(line_d)
                                            part4 = str(line_f)
                                            newline = "\n"
                                            o.write(part1+part2+part3+part4+str(inurl)+newline)





sit = StringVar()

def ex1t():
	root.destroy()

BOX5 = LabelFrame(root,text='MAIN')
ttk.Button(BOX5,text='start',command=test).pack(side=LEFT)
ttk.Button(BOX5,text='exit',command=ex1t).pack(side=LEFT)
Label(BOX5,text='site:(oprnal) :').pack(side=LEFT)
Entry(BOX5, width='4', textvariable=sit).pack(side=LEFT)
BOX5.grid(row=2,columnspan=3)




root.mainloop()
os.remove("date.txt")
os.remove("date1.txt")
os.remove("date2.txt")
os.remove("date3.txt")
os.remove("date4.txt")

"""
               z
             z"F"$$.
       -%- . Led$$$$P-
              3$3 F3$%
              " ^  .3""
                 d***$$e.
              r .%     ^"%
              '$$r
               3$$  *$*$$$$$
                '$$. *b'b"$*$.
                  *$. "L^L"b"$-
                   "$b '. L^b^$
                    ^$$bJ  \ b^$ .
                    b *$$$b.\ \ b \
                    *$."$$$$$b.. % %
                    4$$r'$$b *$.%.\ ".
                    ^$$  $$P  "$.'c^c"e
                    4P"  $F%   '$.'c^r*$c
                    $    $      '$.'c^c "$-
                   $%   .$       '$.'L^b
           J$$$$$$$$$$$$$$$$$$     *.JL.b    byERROR109
"""
