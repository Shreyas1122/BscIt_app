from tkinter import *
import webbrowser
import mysql.connector

def scroll_screen(screen):
    main_frame=Frame(screen)
    main_frame.pack(fill=BOTH,expand=1)
    mycanvas=Canvas(main_frame)
    mycanvas.pack(side="left",fill=BOTH,expand=1)
    #ADD A SCROLLBAR
    myscroll=Scrollbar(main_frame,orient=VERTICAL,command=mycanvas.yview)
    myscroll.pack(side="right",fill=Y)
    #configure the canvas
    mycanvas.configure(yscrollcommand=myscroll.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))
    return mycanvas
def openlink(linked):
    webbrowser.open(linked)
    
def Lang_section(name):
    global languages
    languages=Frame(second_frame,height=80,width=380,bg="#E2E2E2",relief="raised",highlightthickness=2,highlightbackground="black")
    languages.pack(side="top",pady=3)
    languages.pack_propagate(False)
    l1=Label(languages,text=name,font="TimesNewRoman 19 bold",bg="#E2E2E2")
    l1.pack(side="top")
def sub_langsection(name):
    global sublang
    sublang=Frame(second_frame1,height=80,width=380,bg="#E2E2E2",relief="raised",highlightthickness=2,highlightbackground="black")
    sublang.pack(side="top",pady=3)
    sublang.pack_propagate(False)
    l1=Label(sublang,text=name,font="TimesNewRoman 10 bold",bg="#E2E2E2")
    l1.pack(side="top")
def button(link):
    b1=Button(sublang,text="Go to video",command=lambda:openlink(link))
    b1.pack(side="left",pady=10,padx=50)
def pybutton(link):
    b1=Button(python_sub,text="Go to video",command=lambda:openlink(link))
    b1.pack(side="left",pady=10,padx=50)
def notesbutton(var,link):
    b1=Button(var,text="Go to Notes",command=lambda:openlink(link))
    b1.pack(side="left",pady=10,padx=34)
def all_button(frame,link):
    b1=Button(frame,text="Go to video",command=lambda:openlink(link))
    b1.pack(side="top",pady=10)
    
def newversionscreen(sub):
    global newversionscreen
    newversionscreen=Toplevel()
    newversionscreen.geometry('400x580')
    newversionscreen.title("Upcoming Syllabus")
    newversionscreen.minsize(400,580)
    newversionscreen.maxsize(400,580)
    u=Label(newversionscreen,text=f"The Syallbus is coming Soon for '{sub}'\n Thanks for your Patience")
    u.pack()
    newversionscreen.mainloop()
    
    
    
    

def python_sublang(name):
    global python_sub
    python_sub=Frame(second_frame2,height=80,width=380,bg="#E2E2E2",relief="raised",highlightthickness=2,highlightbackground="black")
    python_sub.pack(side="top",pady=3)
    python_sub.pack_propagate(False)
    l1=Label(python_sub,text=name,font="TimesNewRoman 10 bold",bg="#E2E2E2")
    l1.pack(side="top")
def all_sublang(frame,name):
    global all_sub
    all_sub=Frame(frame,height=80,width=380,bg="#E2E2E2",relief="raised",highlightthickness=2,highlightbackground="black")
    all_sub.pack(side="top",pady=3)
    all_sub.pack_propagate(False)
    l1=Label(all_sub,text=name,font="TimesNewRoman 10 bold",bg="#E2E2E2")
    l1.pack(side="top")
    

    
    
    
def cpplang():
    global cppscreen
    cppscreen=Toplevel()
    cppscreen.geometry('400x580')
    cppscreen.title("cpp syllabus")
    y=scroll_screen(cppscreen)
    global second_frame1
    second_frame1=Frame(y)
    y.create_window((0,0),window=second_frame1,anchor="nw")
    sub_langsection("01. Introduction to Cpp(what is cpp,features,installation,\nfirst program)")
    button("https://youtu.be/dCNSDeeKCfs?si=ANk_jzGyVQ2X7Exb")
    notesbutton(sublang,"https://drive.google.com/file/d/1wG50yowP-FRpi4ckB7CXhzdxgaBcZ7aj/view?usp=drive_link")
    sub_langsection("02. what are Datatypes in cpp")
    button("https://youtu.be/MiK5tamc-HE?si=dquAegwY4VbbfIUF")
    notesbutton(sublang,"https://drive.google.com/file/d/12ZTvHhbcO0sjYpFJ6tQtn-v9lw-teNEq/view?usp=drive_link")
    sub_langsection("03. what is variable  in cpp")
    button("https://youtu.be/Ez1RTEXfLSw?si=xPFeeJUtsacCMkiF")
    notesbutton(sublang,"https://www.w3schools.com/cpp/cpp_variables.asp#:~:text=Variables%20are%20containers%20for%20storing,such%20as%20123%20or%20%2D123")
    sub_langsection("04. what are the  keywords  in cpp")
    button("https://youtu.be/iI8fyVPR9FQ?si=nBcJUIV5VnthVasB")
    notesbutton(sublang,"https://www.educba.com/c-plus-plus-keywords/")
    sub_langsection("05. what are header files in cpp")
    button("https://youtu.be/oy7qeDW7OPw?si=akQHytJEm5KSdqzE")
    notesbutton(sublang,"https://www.geeksforgeeks.org/header-files-in-c-c-with-examples/")
    sub_langsection("06. what are  types header files in cpp")
    button("https://youtu.be/oy7qeDW7OPw?si=akQHytJEm5KSdqzE")
    notesbutton(sublang,"https://www.geeksforgeeks.org/header-files-in-c-c-with-examples/")
    sub_langsection("07. what is namespace in cpp")
    button("https://youtu.be/xzvp39aLs1Y?si=X6qB3zaWi4TZb-RG")
    notesbutton(sublang,"https://www.tutorialspoint.com/cplusplus/cpp_namespaces.htm")
    sub_langsection("08. what are operators  in cpp")
    button("https://youtu.be/ZcoL2TxqrsE?si=joJMV4wYLRQvAva2")
    notesbutton(sublang,"https://blog.hubspot.com/website/c-operators")
    sub_langsection("9. what are the conditional statements in cpp")
    button("https://youtu.be/nacpUa54mCI?si=cr2vMvhzlMKnjiVl")
    notesbutton(sublang,"https://topperworld.in/conditional-statements-in-cpp/")
    sub_langsection("10. what is the switch operator in cpp")
    button("https://youtu.be/7X33c1zmfPQ?si=PbSOqTJZKJKgBc1e")
    notesbutton(sublang,"https://codescracker.com/cpp/cpp-switch-statement.htm")
    sub_langsection("11. what is loops  in cpp(types of loops in cpp)")
    button("https://youtu.be/S3XypNZVVLw?si=EDBWxm-5UDnNH7QZ")
    notesbutton(sublang,"https://qti.stu.edu.iq/wp-content/uploads/2019/12/clec10-11.docx.pdf")
    sub_langsection("12. what are functions in cpp")
    button("https://youtu.be/TcNBtrG1We4?si=-Vg-qv0THHeaxaW1")
    notesbutton(sublang,"https://sci.mu.edu.iq/wp-content/uploads/2015/08/C-8.pdf")
    sub_langsection("13. what is structure in cpp")
    button("https://youtu.be/-bscq77n5IE?si=9g10r-laWicxLpks")
    notesbutton(sublang,"https://chavanpragatip.files.wordpress.com/2018/09/structutes-in-c.pdf")
    sub_langsection("14. what is Union in cpp")
    button("https://youtu.be/j3XxAE2cSSY?si=PgK7WVAHS-oLdRHL")
    notesbutton(sublang,"https://www.educative.io/answers/what-are-unions-in-cpp")
    sub_langsection("15. what is array in cpp")
    button("https://youtu.be/40x3FCbeEKk?si=Ku5jnCV-grPEC6xJ")
    notesbutton(sublang,"https://cplusplus.com/doc/tutorial/arrays/")
    sub_langsection("16. what is pointer in cpp")
    button("https://youtu.be/Ms75d_pCgIw?si=5m8Kem9PRqsK6N90")
    notesbutton(sublang,"https://codescracker.com/cpp/cpp-pointers.htm")
    sub_langsection("17. pointer to Array in cpp")
    button("https://youtu.be/NVo1Nns6DSc?si=h9i8YhvVgFTwJHvE")
    notesbutton(sublang,"https://codescracker.com/cpp/cpp-pointers.htm")
    sub_langsection("18. pointer to pointer in cpp")
    button("https://youtu.be/5u-6p4w3PQg?si=mLj1lL-tUJfLx3oD")
    notesbutton(sublang,"https://www.tutorialspoint.com/cplusplus/cpp_pointer_to_pointer.htm")
    sub_langsection("19. pointer to structure in cpp")
    button("https://youtu.be/BjtgpFtBaMo?si=XKCd-giu2Sv42Dot")
    notesbutton(sublang,"https://www.geeksforgeeks.org/cpp-pointer-to-structure/")
    sub_langsection("20. pointer to function in cpp")
    button("https://youtu.be/je7aPo0JScU?si=Gx-yvceTQc_QdSjV")
    notesbutton(sublang,"https://www.javatpoint.com/function-pointer-in-cpp")
    sub_langsection("21. pointer as  function Argumets in cpp")
    button("https://youtu.be/DPBhgUc2-rw?si=hIf4Xm5e8Sj7k_xE")
    notesbutton(sublang,"https://codescracker.com/cpp/cpp-pointers.htm")
    sub_langsection("22. recursion in cpp")
    button("https://youtu.be/_-2u4EPHD88?si=4KvkfW4cv2ItCFTw")
    notesbutton(sublang,"https://favtutor.com/blogs/recursion-cpp")
    sub_langsection("23. what is OOPS(object oriented language)")
    button("https://youtu.be/i2OOPAvCDK0?si=JNAYQpd1zF4M-Xne")
    notesbutton(sublang,"https://drive.google.com/file/d/1wG50yowP-FRpi4ckB7CXhzdxgaBcZ7aj/view?usp=drive_link")
    sub_langsection("24. features of OOPS(object oriented language)")
    button("https://youtu.be/b3GccK5_KSQ?si=M6UM86_y02MIxH8N")
    notesbutton(sublang,"https://www.interviewbit.com/blog/features-of-oops/")
    sub_langsection("25. oops concepts(Objects,classes,constructor,\ndeconstructor,const and static keyword)")
    button("https://youtu.be/i_5pvt7ag7E?si=KuZ4hcTlzc3yU7hs")
    notesbutton(sublang,"https://drive.google.com/file/d/19x9iCEzGDV9yTbtY6IcGRn5MhOhV8y7a/view?usp=drive_link")
    sub_langsection("26. Dynamic Memory Allocation in cpp ")
    button("https://youtu.be/MMO2c57XHzM?si=nOnLCIs5dae_YjLd")
    notesbutton(sublang,"")
    sub_langsection("27. File Handling in cpp ")
    button("https://youtu.be/OJ8KYsaneZM?si=vKHM8lib-6SLzEPD")
    notesbutton(sublang,"https://www.codingninjas.com/studio/library/file-handling-in-cpp")
    sub_langsection("28. STL(standard template library) in cpp ")
    button("https://youtu.be/WgMPrLX-zsA?si=rfrT5E46-zBBU0i-")
    notesbutton(sublang,"https://www.javatpoint.com/cpp-stl-components")
    
def pythonlangpage():
    global pyscreen
    pyscreen=Toplevel()
    pyscreen.geometry('400x580')
    pyscreen.title("python syllabus")
    y=scroll_screen(pyscreen)
    global second_frame2
    second_frame2=Frame(y)
    y.create_window((0,0),window=second_frame2,anchor="nw")
    python_sublang("01. Introduction to python(what is python,features,\ninstallation,first program)")
    pybutton("https://youtu.be/qYhrd2Lhq0g?si=W2zavrVvbHkHP_Nf")
    notesbutton(python_sub,"https://drive.google.com/file/d/1FnKkJpwWYaaTE5cGVl1rvbWi8llP6O1M/view?usp=drive_link")
    python_sublang("02.What is Interpreted and compiling Languages ?")
    pybutton("https://youtu.be/QNBKWHneOxk?si=BrekLz0c6BQmucZE")
    notesbutton(python_sub,"https://byjusexamprep.com/liveData/f/2023/5/difference_between_compiler_and_interpreter_gate_notes_59.pdf")
    python_sublang("03.Variables  and datatypes in Python")
    pybutton("https://youtu.be/k0ZAkmYxVTQ?si=U469ewsIhk-mSM2j")
    notesbutton(python_sub,"https://drive.google.com/file/d/17XfC6xGqytmxIBmbe7I3eF8q3Btbm8kQ/view?usp=drive_link")
    python_sublang("04.operators in Python")
    pybutton("https://youtu.be/uqPIk_0q940?si=t6hoBx3U_rH9JGHt")
    notesbutton(python_sub,"https://isip.piconepress.com/courses/temple/ece_3822/resources/tutorials/python/python_basic_operators.pdf")
    python_sublang("05.loops in Python(for loop,while loop)")
    pybutton("https://youtu.be/DjsCmmMua1Y?si=6r5jv-0GNWY7D3ST")
    notesbutton(python_sub,"https://mitu.co.in/wp-content/uploads/2017/09/Python-Pt-4-Looping.pdf")
    python_sublang("06.Conditional Statements in python(if,elif,else)")
    pybutton("https://youtu.be/5QlCw1_N6xk?si=V6ubDzRGSXt9NmbH")
    notesbutton(python_sub,"https://pythonclassroomdiary.files.wordpress.com/2019/07/conditionalstatements.pdf")
    python_sublang("08.String in python")
    pybutton("https://youtu.be/esnhngyUMRc?si=l6OK_7fkK04gCf3m")
    notesbutton(python_sub,"https://www.dspmuranchi.ac.in/pdf/Blog/Python%20String%20and%20python%20string%20methods.pdf")
    python_sublang("09.List in python")
    pybutton("https://youtu.be/SkFidEd3f_0?si=BesmD2WiS_f7MpBX")
    notesbutton(python_sub,"https://www.tutorialspoint.com/python/pdf/python_lists.pdf")
    python_sublang("10.Dictionary in python")
    pybutton("https://youtu.be/xhjdfmu0FVA?si=PMkYgkAgK5yTRzNt")
    notesbutton(python_sub,"https://www.tutorialspoint.com/python/pdf/python_dictionary.pdf")
    python_sublang("11.Tuple in python")
    pybutton("https://youtu.be/nlyQTx3cq9w?si=IvdV74MM494QiUO")
    notesbutton(python_sub,"https://www.tutorialspoint.com/python/pdf/python_tuples.pdf")
    python_sublang("12.Set in python")
    pybutton("https://youtu.be/5S8VNzyUZl4?si=wrGoxe0VDiRCodUf")
    notesbutton(python_sub,"https://www.tutorialkart.com/pdf/python/python-sets.pdf")
    python_sublang("13.Functions in python")
    pybutton("https://youtu.be/DsCazsOPHSc?si=6Lg7Bhh6siYfUkXs")
    notesbutton(python_sub,"https://www.tutorialspoint.com/python/pdf/python_functions.pdf")
    python_sublang("14.Module in python")
    pybutton("https://youtu.be/NJ_JTzpjKE8?si=Y-nmxCUqbi1J3qCA")
    notesbutton(python_sub,"https://drive.google.com/file/d/1il24avXFt7_PX5ddfiot7CEkKuHsWLF0/view?usp=drive_link")
    python_sublang("15.Random Module in python")
    pybutton("https://youtu.be/0V8VTMol7Vc?si=lj1-S7c2YPWlpFDA")
    notesbutton(python_sub,"https://www.pythoncheatsheet.org/modules/random-module")
    python_sublang("16.Datetime Module in python")
    pybutton("https://youtu.be/V9XGDk1oF3k?si=4Tge4B-9JTBCkcPr")
    notesbutton(python_sub,"https://littleflowercollege.edu.in/upload/e_contents/files/34e4e814f4886bc7347f742748ad8dfc.pdf")
    python_sublang("17.Pickle Module in python")
    pybutton("https://youtu.be/Kcds00lK4Dw?si=FPQ5j5tVUtgMYfTD")
    notesbutton(python_sub,"https://www.javatpoint.com/pickle-module-of-python")
    python_sublang("18.File Handling in python")
    pybutton("https://youtu.be/UCKbrAoFUlM?si=XTeLVCcgNGa-pcGK")
    notesbutton(python_sub,"https://www.cs2study.com/XII/filehandling/file%20handling%20python%20notes.pdf")
    python_sublang("19.Exception Handling in python")
    pybutton("https://youtu.be/qrueF1F9ndE?si=whsmd7Gq7hKBkvke")
    notesbutton(python_sub,"")
    python_sublang("20.OOPS(classes and objects)\n in python")
    pybutton("https://youtu.be/bjM1JjGzvb8?si=bkSiX8KJumBIAZe4")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/python-oops-concepts/")
    python_sublang("21.OOPS(Methods and Constuctors)\n in python")
    pybutton("https://youtu.be/qz_bnx84Xe0?si=zsO-jKEoe42hm9-c")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/python-oops-concepts/")
    python_sublang("22.OOPS(Polymorphism)\n in python")
    pybutton("https://youtu.be/drb9efyRMOM?si=1EvmBvOJcA6bQ86D")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/python-oops-concepts/")
    python_sublang("23.OOPS(inheritance)\n in python")
    pybutton("https://youtu.be/w2jV9qZ6PGo?si=zmQ8cqJG69vGCac6")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/python-oops-concepts/")
    python_sublang("24.OOPS(Encapsulation)\n in python")
    pybutton("https://youtu.be/3V90qEND-1o?si=qRk3d3pTYHq0G_ea")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/python-oops-concepts/")
    python_sublang("25.OOPS(Abstraction)\n in python")
    pybutton("https://youtu.be/e8xctqrzSSA?si=UMYcQ1DTNQbhR__N")
    notesbutton(python_sub,"https://www.slideshare.net/karu43/pythondataabstarctionpptx")
    python_sublang("26.Multithreading in python")
    pybutton("https://youtu.be/xcF4ypUW6e4?si=HiPh6hgDf12Nm3Sr")
    notesbutton(python_sub,"https://www.javatpoint.com/multithreading-in-python-3")
    python_sublang("27.Tkinter(GUI)(full playlist) in python")
    pybutton("https://youtu.be/-Q4lm8eYulw?si=12nfb9UxJp4Hv1D3")
    notesbutton(python_sub,"https://pythontrends.files.wordpress.com/2019/08/introduction-to-tkinter-for-gui-application-1.pdf")
    python_sublang("28.connecting GUI with MYsql in python")
    pybutton("https://youtu.be/MhaH7o3lf4E?si=-OA5_OzytrpzAk8D")
    notesbutton(python_sub,"https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/")
    python_sublang("29.creating small project with Mysql in python")
    pybutton("https://youtu.be/TMfKX5uIX3Y?si=ev2VNmsNgMvoeWid")
   
    
    
def java_lang():
    global java_screen
    java_screen=Toplevel()
    java_screen.geometry('400x580')
    java_screen.title("Java syllabus")
    y=scroll_screen(java_screen)
    global second_frame3
    second_frame3=Frame(y)
    y.create_window((0,0),window=second_frame3,anchor="nw")
    all_sublang(second_frame3,"01. Introduction to Java(what is Java)")
    all_button(all_sub,"https://youtu.be/WYpQ1VkXag0?si=TENODPwoEXra9KSx")
    all_sublang(second_frame3,"02. Features of Java")
    all_button(all_sub,"https://youtu.be/7uPKIffcXuc?si=ZE0Dtp8urRRQXgV0")
    all_sublang(second_frame3,"03. Why Java is Platform independent Language")
    all_button(all_sub,"https://youtu.be/mJxS8Hy8U88?si=TOHX7Poi4sZLF7y8")
    all_sublang(second_frame3,"04. History Of Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=1105")
    all_sublang(second_frame3,"05.What is JVM in Java")
    all_button(all_sub,"https://youtu.be/YcJyY9g7L1s?si=2Ebc052UZauM7Aus")
    all_sublang(second_frame3,"06. What is OOPS(object Oriented Programing)\n in Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=2634")
    all_sublang(second_frame3,"07. objects and classes in java")
    all_button(all_sub,"https://youtu.be/L677QCBCuWk?si=w79ZnSNJLQcupESH")
    all_sublang(second_frame3,"08. Constructors in java")
    all_button(all_sub,"https://youtu.be/Y1lP07CFP0Y?si=bRGYYtNItcIDv9Xq")
    all_sublang(second_frame3,"09. Basic Structure of Java Program")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=3972")
    all_sublang(second_frame3,"10. What is JDK vs JRE vs JVM")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=4414")
    all_sublang(second_frame3,"11. What are different files generated in Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=4328")
    all_sublang(second_frame3,"12. Installation of JDK for Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=2993")
    all_sublang(second_frame3,"13. First Basic Progam of Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=3315")
    all_sublang(second_frame3,"14. Installation of IDE for Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=5650")
    all_sublang(second_frame3,"15. Variables and DataTypes in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=8073")
    all_sublang(second_frame3,"16. KeyWords in Java ")
    all_button(all_sub,"https://youtu.be/ZWRE0WuP-jw?si=2u0eJFcTN8D7394h")
    all_sublang(second_frame3,"17. Escape Sequence in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=10878")
    all_sublang(second_frame3,"18. User Input In Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=11579")
    all_sublang(second_frame3,"19. Typecasting In Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=12703")
    all_sublang(second_frame3,"20. operators In Java ")
    all_button(all_sub,"https://youtu.be/xKu0JL9L12I?si=NPRS6ibxMF7miIIn")
    all_sublang(second_frame3,"21.  Types of operators and If-Else Statements In Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=13523")
    all_sublang(second_frame3,"22.  Introduction To Number Sytem in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=24110")
    all_sublang(second_frame3,"23.  Introduction To Bitwise operator in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=24708")
    all_sublang(second_frame3,"24.   Some Quiz Questions for practice (part 1)")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=eX_b1sJ4a4s_iN9b&t=25095")
    all_sublang(second_frame3,"25.   loops in Java ")
    all_button(all_sub,"https://youtu.be/0r1SfRoLuzU?si=PrA8Zuca49py4cXF")
    all_sublang(second_frame3,"26.   Comments in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=eX_b1sJ4a4s_iN9b&t=26703")
    all_sublang(second_frame3,"27.   what are methods/functions in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=eX_b1sJ4a4s_iN9b&t=27974")
    all_sublang(second_frame3,"28.   what are return statements of  in Java ")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=eX_b1sJ4a4s_iN9b&t=30177")
    all_sublang(second_frame3,"29.   what is difference between parameter and Argument")
    all_button(all_sub,"https://youtu.be/D33u0pGBChk?si=ceEQ_i39fSmJQ44I")
    all_sublang(second_frame3,"30.   Some Quiz Questions for practice(part 2)")
    all_button(all_sub,"https://youtu.be/D33u0pGBChk?si=ceEQ_i39fSmJQ44I")
    all_sublang(second_frame3,"31.   What is Array In Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=39733")
    all_sublang(second_frame3,"32.   what are different types of methods in java")
    all_button(all_sub,"https://youtu.be/86B96Fy6j6U?si=nAoC-Kc2vLmVIWCg")
    all_sublang(second_frame3,"32.   What is 2D Array In Java")
    all_button(all_sub,"https://youtu.be/PymbRTMb4hY?si=-1IeffugF80DJyxf&t=41975")
    
    
    
    
    
    
def Page():
    root=Tk()
    root.geometry('400x580')
    root.title("Topics")
    root.maxsize(400,580)
    root.minsize(400,580)
    x=scroll_screen(root)
    global second_frame
    second_frame=Frame(x)
    x.create_window((0,0),window=second_frame,anchor="nw")
    second_frame=Frame(x)
    x.create_window((0,0),window=second_frame,anchor="nw")    
    Lang_section("01.  Python ")
    b1=Button(languages,text="Go to Chapters",command=pythonlangpage)
    b1.pack(side="top",pady=10)
    Lang_section("02.   C++     ")
    b2=Button(languages,text="Go to Chapters",command=cpplang)
    b2.pack(side="top",pady=10)
    Lang_section("03.    C       ")
    b3=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("c language"))
    b3.pack(side="top",pady=10)
    Lang_section("04.   Java   ")
    b4=Button(languages,text="Go to Chapters",command=java_lang)
    b4.pack(side="top",pady=10)
    Lang_section("05.   Flutter")
    b5=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("flutter"))
    b5.pack(side="top",pady=10)
    Lang_section("06.   Mysql")
    b6=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("Mysql"))
    b6.pack(side="top",pady=10)
    Lang_section("07.   sql    ")
    b7=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("sql"))
    b7.pack(side="top",pady=10)
    Lang_section("08.   Html  ")
    b8=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("html"))
    b8.pack(side="top",pady=10)
    Lang_section("09.   Css  ")
    b9=Button(languages,text="Go to Chapters",command=lambda:newversionscreen("css"))
    b9.pack(side="top",pady=10)
    root.mainloop()

con=mysql.connector.connect(host='localhost',password='shreyas@29',user='root')
cur=con.cursor(buffered=True)
try:
    cur.execute("use login_signup;")
    con.commit()
except:
    cur.execute("create database login_signup;")
    con.commit()

try:
    cur.execute("describe login_table;")
    con.commit()
except:
    cur.execute("create table login_table(username varchar(20),password  varchar(20),con_password varchar(20));")
    con.commit()

def successfulpage():
    if(len(se1.get())==0 or len(se2.get())==0 or len(se3.get())==0):
        l=Label(f33,text="All the Entries should be Filled",fg="red")
        l.pack(side="top")
    else:
        global lulla
        if(se2.get()==se3.get()):
            cur.execute(f"insert into login_table(username,password,con_password) values('{se1.get()}','{se2.get()}','{se3.get()}');")
            con.commit()
            Page()
            try:
                lulla.destroy()
            except:
                lulla=Label()
             
        else:
            lulla=Label(f33,text="please enter the password that matches previous one",fg="red")
            lulla.pack(side="top")
       


def signup():
    global signup_window
    signup_window=Toplevel()
    signup_window.title("Signup")
    signup_window.config(bg="white")
    signup_window.geometry('800x700')
    signup_window.maxsize(800,700)
    signup_window.minsize(800,700)
    global f11
    f11=Frame(signup_window)
    f11.pack(side="top")
    sl0=Label(f11,text="SIGN IN",font="TimesNewRoman  40 bold").pack(side="top",pady=45,)
    global sl1
    sl1=Label(f11,text="Enter your username*",font="TimesNewRoman 22 bold")
    sl1.pack(side="top")
    global se1
    se1=Entry(f11,width=30,font="TimesNewRoman 18 ",relief="solid",)
    se1.pack(side="top")
    se1.bind('<FocusIn>',focusin2)
    se1.bind('<FocusOut>',focusout2)
    global f22
    f22=Frame(signup_window)
    f22.pack(side="top",pady=50)
    global sl2
    sl2=Label(f22,text="Enter your  password*",font="TimesNewRoman 22 bold")
    sl2.pack(side="top")
    global se2
    se2=Entry(f22,width=30,font="TimesNewRoman 18 ",relief="solid")
    se2.pack(side="top")
    se2.bind('<FocusIn>',focusin3)
    se2.bind('<FocusOut>',focusout3)
    global sl3
    global se3
    global f33
    f33=Frame(signup_window)
    f33.pack(side="top")
    sl3=Label(f33,text="Confirm the password*",font="TimesNewRoman 22 bold",)
    sl3.pack(side="top",pady=10)
    se3=Entry(f33,width=30,font="TimesNewRoman 18",relief="solid")
    se3.pack(side="top")
    se3.bind('<FocusIn>',focusin4)
    se3.bind('<FocusOut>',focusout4)
    global f44
    f44=Frame(signup_window)
    f44.pack(side="top")
    b1=Button(f44,text="Sign Up",command=successfulpage,font="TimesNewRoman 17 bold",bg="yellow")
    b1.pack(side="top")
    signup_window.mainloop()

def newscreen(par):
    global page1
    page1=Toplevel()
    page1.title(par)
    page1.config(bg="white")
    page1.geometry('800x700')
    page1.maxsize(800,700)
    page1.minsize(800,700)
    f1=Frame(page1)
    f1.pack()
    l1=Label(f1,text="login or sign up successfully my dear",font="TimesNewRoman 22 bold").pack(side="top")
    

def loginsuccessful():
    global y
    cur.execute("select username,password from login_table;")
    result=cur.fetchall()
    for i in result:
        for j in range(0,1,1):
            if(i[j]==e1.get() and i[1]==e2.get()):
                Page()
            else:
                try:
                    k=y.winfo_exists()
                    if(k==1):
                        pass
                except:
                    y=Label(hh,text="Please Enter The Correct Username or Password",fg="red")
                    y.pack(side="top")
                
    con.commit()

def update_password():
    cur.execute("select username from login_table;")
    result=cur.fetchall()
    for i in result:
        for j in range(0,1,1):
            if(i[j]==se5.get()):
                cur.execute(f"UPDATE login_table SET password='{se6.get()}',con_password='{se6.get()}' WHERE username='{se5.get()}'")
                con.commit()
                l=Label(f77,text="password changes successfully").pack(side="top")
def update_passwordwindow():
    global pager
    pager=Toplevel()
    pager.title("Update password")
    pager.config(bg="white")
    pager.geometry('800x700')
    pager.maxsize(800,700)
    pager.minsize(800,700)
    f1=Frame(pager)
    f1.pack()
    l=Label(f1,text="Update the password",font="TimesNewRoman 22 bold")
    l.pack(side="top")
    global f55
    f55=Frame(pager)
    f55.pack(side="top",pady=50)
    global sl5
    sl5=Label(f55,text="Enter your username associate with Account*",font="TimesNewRoman 22 bold")
    sl5.pack(side="top")
    global se5
    se5=Entry(f55,width=30,font="TimesNewRoman 18 ",relief="solid")
    se5.pack(side="top")
    se5.bind('<FocusIn>',focusin6)
    se5.bind('<FocusOut>',focusout6)
    global f66
    global sl6
    global se6
    f66=Frame(pager)
    f66.pack(side="top")
    sl6=Label(f66,text="Confirm the password*",font="TimesNewRoman 22 bold",)
    sl6.pack(side="top",pady=10)
    se6=Entry(f66,width=30,font="TimesNewRoman 18",relief="solid")
    se6.pack(side="top")
    se6.bind('<FocusIn>',focusin7)
    se6.bind('<FocusOut>',focusout7)
    global f77
    f77=Frame(pager)
    f77.pack(side="top")
    b=Button(f77,text="confirm",command=update_password).pack(side="top")
    
    
    
def focusin(event):
    e1.config(highlightthickness=3, highlightbackground="red")
    l1.config(fg="red")
    
    
def focusout(event):
    e1.config(highlightthickness=1, highlightbackground="black")
    l1.config(fg="black")
    
    if(len(e1.get())==0):
        global lab
        lab=Label(f1,text="please Enter any username",fg="red")
        lab.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab.destroy()
        except:
            lab=Label()
        
def focusin1(event):
    e2.config(highlightthickness=3, highlightbackground="red")
    l2.config(fg="red")
def focusout1(event):
    e2.config(highlightthickness=1, highlightbackground="black")
    l2.config(fg="black")
    if(len(e2.get())==0):
        global labb
        labb=Label(f,text="please Enter any Password",fg="red")
        labb.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            labb.destroy()
        except:
            labb=Label()
def focusin2(event):
    se1.config(highlightthickness=3, highlightbackground="red")
    sl1.config(fg="red")
def focusout2(event):
    se1.config(highlightthickness=1, highlightbackground="black")
    sl1.config(fg="black")
    if(len(se1.get())==0):
        global lab1
        lab1=Label(f11,text="please Enter any username",fg="red")
        lab1.pack(side="top")
    else:
        try:
            lab1.destroy()
        except:
            lab1=Label()
        
def focusin3(event):
    se2.config(highlightthickness=3, highlightbackground="red")
    sl2.config(fg="red")
def focusout3(event):
    se2.config(highlightthickness=1, highlightbackground="black")
    sl2.config(fg="black")
    if(len(se2.get())==0):
        global lab2
        lab2=Label(f22,text="please Enter a password(Including special characters,uppercase,numbers)",fg="red")
        lab2.pack(side="top")
    else:
        try:
            lab2.destroy()
        except:
            lab2=Label()
        

    
def focusin4(event):
    se3.config(highlightthickness=3, highlightbackground="red")
    sl3.config(fg="red")
def focusout4(event):
    se3.config(highlightthickness=1, highlightbackground="black")
    sl3.config(fg="black")
    if(len(se3.get())==0):
        global lab3
        lab3=Label(f33,text="please Enter to confirm password",fg="red")
        lab3.pack(side="top")
        
    else:
        try:
            lab3.destroy()
        except:
            lab3=Label()
def focusin6(event):
    se5.config(highlightthickness=3, highlightbackground="red")
    sl5.config(fg="red")
def focusin7(event):
    se6.config(highlightthickness=3, highlightbackground="red")
    sl6.config(fg="red")
def focusout6(event):
    se5.config(highlightthickness=1, highlightbackground="black")
    sl5.config(fg="black")
    if(len(se5.get())==0):
        global lab355
        lab355=Label(f55,text="please enter your old username correctly",fg="red")
        lab355.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab355.destroy()
        except:
            lab355=Label()
def focusout7(event):
    se6.config(highlightthickness=1, highlightbackground="black")
    sl6.config(fg="black")
    if(len(se6.get())==0):
        global lab333
        lab333=Label(f66,text="please Enter to confirm password",fg="red")
        lab333.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab333.destroy()
        except:
            lab333=Label()





    
    
root=Tk()
f1=Frame(root)
root.geometry('800x600')
root.maxsize(800,600)
root.minsize(800,600)
f1.pack(side="top")
l0=Label(f1,text="LOGIN",font="TimesNewRoman  40 bold").pack(side="top",pady=45,)
l1=Label(f1,text="Enter your username*",font="TimesNewRoman 22 bold")
l1.pack(side="top")
e1=Entry(f1,width=30,font="TimesNewRoman 18 ",relief="solid",)
e1.pack(side="top")
e1.bind('<FocusIn>',focusin)
e1.bind('<FocusOut>',focusout)
f2=Frame(root)
f2.pack(side="top",pady=50)
f=Frame(f2)
l2=Label(f2,text="Enter your password*",font="TimesNewRoman 22 bold")
l2.pack(side="top")
e2=Entry(f2,width=30,font="TimesNewRoman 18 ",relief="solid")
e2.pack(side="top")
e2.bind('<FocusIn>',focusin1)
e2.bind('<FocusOut>',focusout1)
f.pack(side="top")
v=Button(f2,text="Forgot my password ?",command=update_passwordwindow)
v.pack(side="top",pady=10)
Label(f2,text="New here ?",font="TimesNewRoman 15 bold",fg="blue").pack(side="left",padx=65,pady=20)
bu=Button(f2,text="Sign In",command=signup,bg="blue",fg="white")
bu.pack(side="left")
hh=Frame(root)
hh.pack(side="top")
f3=Frame(root)
f3.pack(side="top")
b1=Button(f3,text="Login",command=loginsuccessful,font="TimesNewRoman 17 bold",bg="yellow")
b1.pack(side="top")






root.mainloop()
