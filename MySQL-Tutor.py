from email import contentmanager
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from time import strftime
import datetime as dt
import webbrowser
from collections import Counter
import matplotlib.pyplot as plt

global mysql_connect
mysql_connect="no" 
global mydb
global current_que
current_que=-1
topic_count={}
crct_count={}

def time():
    string = strftime('%H:%M:%S')
    now.config(text = string)
    now.after(1000, time)

def connect():
    #Connection establishment 
    name,pwd = getcredentials()
    if name=='' or pwd=='':
        messagebox.showwarning('Warning!', 'Please enter the required details!')
    else:
        try:
            global mydb
            mydb = mysql.connector.connect(host="localhost",user=name,password=pwd)
            mycursor = mydb.cursor()
            global mysql_connect
            mysql_connect="yes"
            ui_next_frame.grid(row=0,column=1,sticky='nsew',columnspan=2)
            ui_next_frame.tkraise()
            
        except mysql.connector.Error as err:
            mysql_connect="no"
            messagebox.showwarning('Warning!','Problem connecting to your MySQl Application\nKindly check your credentials\nYou might have entered your password Wrong\nError No.: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))


def getcredentials():
    return username.get(),password.get()

def ui1_frame():
    if mysql_connect == "yes": 
        messagebox.showinfo("Tip","If you are strong at your basics you can directly go to Level II")
        ui_frame_level1.grid(row=0,column=0,rowspan=3,sticky='nsew')
        ui_frame_level1.tkraise()      
    else:
        messagebox.showwarning("Need MySQL Connection!","You need to establish a connection between your MySQL tool and this application.\nPlease enter your valid credentials")

def ui2_frame():
    if mysql_connect == "yes":
        ui_frame_level2.grid(row=0,column=0,rowspan=3,sticky='nsew')
        ui_frame_level2.tkraise() 
        sample_table()    
        tableview_l2() 
    else:
        messagebox.showwarning("Need MySQL Connection!","You need to establish a connection between your MySQL tool and this application.\nPlease enter your valid credentials")

def home():
    time_frame.tkraise()
    main_frame.tkraise()

def open_topic_level1(num):
    global current_que 
    if num==-1:
        default_Que.grid(column=0,columnspan=2,row=0,rowspan=8,sticky='nsew')
        default_Que.tkraise()
        current_que=-1
    elif num==0:
        que0.grid(column=0,columnspan=2,row=0,rowspan=8,sticky='nsew')
        que0.tkraise()
        current_que=num
    elif num==1:
        que1.grid(column=0,columnspan=2,row=0,rowspan=8,sticky='nsew')
        que1.tkraise()
        current_que=num
    elif num==2:
        que2.grid(column=0,columnspan=2,row=0,rowspan=8,sticky='nsew')
        que2.tkraise()
        current_que=num
    elif num==3:
        que3.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que3.tkraise()
        current_que=num
    elif num==4:
        que4.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que4.tkraise()
        current_que=num
    elif num==5:
        que5.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que5.tkraise()
        current_que=num
    elif num==6:
        que6.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que6.tkraise()
        current_que=num
    elif num==7:
        que7.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que7.tkraise()
        current_que=num
    elif num==8:
        que8.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que8.tkraise()
        current_que=num
    elif num==9:
        que9.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que9.tkraise()
        current_que=num                
    elif num==10:
        que10.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que10.tkraise()
        current_que=num 
    elif num==11:
        que11.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que11.tkraise()
        current_que=num 
    elif num==12:
        que12.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que12.tkraise()
        current_que=num 
    elif num==13:
        que13.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que13.tkraise()
        current_que=num 
    elif num==14:
        que14.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que14.tkraise()
        current_que=num 
    elif num==15:
        que15.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que15.tkraise()
        current_que=num 
    elif num==16:
        que16.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que16.tkraise()
        current_que=num 
    elif num==17:
        que17.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que17.tkraise()
        current_que=num 
    elif num==18:
        que18.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que18.tkraise()
        current_que=num 
    elif num==19:
        que19.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que19.tkraise()
        current_que=num 
    elif num==20:
        que20.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que20.tkraise()
        current_que=num 
    elif num==21:
        que21.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que21.tkraise()
        current_que=num 
    elif num==22:
        que22.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que22.tkraise()
        current_que=num 
    elif num==23:
        que23.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
        que23.tkraise()
        current_que=num 
    else:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def alter_subtopic_open():
    choice=que8_optionentry_value.get()
    if choice=="":
        messagebox.showerror("Error",'Please enter a valid number\nYou can only choose between 1 to 4')
        return
    elif choice not in ['1','2','3','4']:
        messagebox.showerror("Error",'Please enter a valid number\nYou can only choose between 1 to 4')
        return
    else:
        choice=int(choice)
        if choice==1:
            que8_1.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
            que8_1.tkraise() 
        elif choice==2:
            que8_2.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
            que8_2.tkraise()
        elif choice==3:
            que8_3.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
            que8_3.tkraise()
        elif choice==4:
            que8_4.grid(column=0,columnspan=2,row=0,rowspan=8,sticky="nsew")
            que8_4.tkraise()
    
def remove_spaces(s):
    while(" " in s):
        s=s.replace(" ","") 
    return s   

def string_comparison(s1,s2):
    res={'Extra' : [],"Missing" : []}
    s1=remove_spaces(s1)
    s2=remove_spaces(s2)
    d1={} 
    d2={} 
    for i in s1:
        if i in d1:
            d1[i]+=1 
        else:
            d1[i]=1 
    for i in s2:
        if i in d2:
            d2[i]+=1 
        else:
            d2[i]=1
    for i in d1.keys():
        if i in d1 and i in d2:
            if d1[i]>d2[i]:
                res['Missing'].append(i)
    d1=Counter(d1) 
    d2=Counter(d2)
    d2=d2-d1 
    res['Extra']=list(d2.keys()) 
    for i in set(s1):
        if i not in s2:
            if i not in res['Missing']:
                res['Missing'].append(i)
    if res["Extra"]==[] and res["Missing"]==[]:
        return False
    return res

def ui_frame_prevtopic():
    global current_que 
    current_que-=1 
    if current_que < -1:
        messagebox.showinfo("info","No more previous topics to view")
        current_que=-1
    open_topic_level1(current_que)

def ui_frame_nexttopic():
    global current_que 
    current_que+=1 
    if current_que>23:
        messagebox.showinfo("info","No more further topics to view\nYou can start Level II Tutoring")
        current_que=23
    open_topic_level1(current_que)

def for_dicts(name,key):
    if key in name:
        name[key]+=1 
    else:
        name[key]=1 

def performance_graphs():
    try:
        result_dic={}
        for i in topic_count.keys():
            if i not in result_dic:
                if i not in crct_count:
                    result_dic[i]=0
                elif topic_count[i]==crct_count[i]:
                    result_dic[i]=100
                else:
                    result_dic[i]=(crct_count[i]/topic_count[i])*100
        names = list(result_dic.keys())
        values = list(result_dic.values())
        fig = plt.figure(0)
        fig.canvas.manager.set_window_title('Performance Graph')
        plt.bar(range(len(result_dic)), values, tick_label=names)
        plt.title("Performance Graph")
        plt.ylabel("Accuracy Rate(%)")
        plt.xlabel("Concepts Covered")
        plt.show()
    except:
        messagebox.showinfo("Sorry for inconvenience","There might be some issue, as of now\nwe can't able to plot your performance graph!\nWe will work on this issue.")

def view_in_detail(num):
    if num==0:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-create-database")   
    elif num==1:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-drop-database")
    elif num==2:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-show-list-databases")
    elif num==3:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-create-table")
    elif num==4:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-drop-table")
    elif num==5:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-rename-table")
    elif num==6:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-primary-key")
    elif num==7:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-foreign-key")
    elif num==8:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-alter-table")
    elif num==9:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-insert")
    elif num==10:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-delete")
    elif num==11:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-update")
    elif num==12:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-select")
    elif num==13:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-show-list-tables")
    elif num==14:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-where")
    elif num==15:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-distinct")
    elif num==16:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-order-by")
    elif num==17:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-group-by")
    elif num==18:
        webbrowser.open_new(r"https://www.javatpoint.com/mysql-having")
    elif num>=19 and num<=23:
        webbrowser.open_new(r"https://www.javatpoint.com/dbms-sql-aggregate-function")
    elif num==24:
        webbrowser.open_new(r"https://dev.mysql.com/downloads/installer/")
    elif num==25:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=WuBcTJnIuzo&t=489s")
    else:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def Run_Query(num):
    global mydb
    mycursor = mydb.cursor()
    full_query=""
    if num==0:
        command=[que0_sol1.get().lower().strip(),que0_sol2.get().lower().strip(),remove_spaces(que0_sol3.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que0_full_query.configure(text='')
            que0_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")            
        elif command[1]!="database" or command[0]!="create":
            que0_full_query.configure(text='')
            que0_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[2]!="tutoringsystem;":
            que0_full_query.configure(text='')
            que0_success_ack.configure(text='')
            messagebox.showerror("Error","Database name should be same as mentioned in the Question\nDon't forgot to use semi-colon")
        else:
            try:
                mycursor.execute("drop database if exists tutoringsystem")
                mycursor.execute(full_query)
                que0_full_query.configure(text="command: create database tutoringsystem;")
                que0_success_ack.configure(text='Well Done! You got it Right')
                for_dicts(crct_count,'DDL')                             
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que0_full_query.configure(text='')
                que0_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,'DDL') 
    elif num==1:
        command=[que1_sol1.get().lower().strip(),que1_sol2.get().lower().strip(),remove_spaces(que1_sol3.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que1_full_query.configure(text='')
            que1_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[1]!="database" or command[0]!="drop":
            que1_full_query.configure(text='')
            que1_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[2]!="tutoringsystem;":
            que1_full_query.configure(text='')
            que1_success_ack.configure(text='')
            messagebox.showerror("Error","Database name should be same as mentioned in the Question\nDon't forgot to use semi-colon")
        else:
            try:
                mycursor.execute("create database if not exists tutoringsystem")
                mycursor.execute(full_query)
                que1_full_query.configure(text="command: drop database tutoringsystem;")
                que1_success_ack.configure(text='Well Done! You got it Right') 
                for_dicts(crct_count,'DDL')               
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que1_full_query.configure(text='')
                que1_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found kindly restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,'DDL')
    elif num==2:
        command=[que2_sol1.get().lower().strip(),remove_spaces(que2_sol2.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="":
            que2_full_query.configure(text='')
            que2_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!='show':
            que2_full_query.configure(text='')
            que2_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[1]!='databases;':
            que2_full_query.configure(text='')
            que2_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nDont forgot to use semi-colon at the end of the query\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        else:
            try:
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que2_success_ack.configure(text='Well Done! You got it Right')
                que2_full_query.configure(text='command: show databases ;') 
                for_dicts(crct_count,'DDL')  
            except mysql.connector.Error as err:
                que2_full_query.configure(text='')
                que2_success_ack.configure(text='')
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!") 
        for_dicts(topic_count,'DDL')
    elif num==3:
        command=[]
        for i in range(1,7):
            s=f'command.append(que{num}_sol{i}.get().strip().lower())'
            exec(s) 
        full_query=" ".join(command)
        que3_mistakes=[]
        l1,l2,l3,l4=0,0,0,0
        if command[0]!="create table":
            messagebox.showerror('Error','Check the syntax properly-create table [table_name]')
            return
        if command[1]!="students":
            messagebox.showerror('Error','table name should be same as mentioned in the question')
            return
        current_cmp=string_comparison('( roll int,',command[2])
        if current_cmp!=False:
            l1=len(current_cmp['Missing'])
            que3_mistakes.append("In 3rd input box, Characters "+str(current_cmp)) 
        current_cmp=string_comparison('name varchar(20),',command[3])
        if current_cmp!=False:
            l2=len(current_cmp['Missing'])
            que3_mistakes.append("In 4th input box, Characters "+str(current_cmp))
        current_cmp=string_comparison('year int,',command[4])
        if current_cmp!=False:
            l3=len(current_cmp['Missing'])
            que3_mistakes.append("In 5th input box, Characters "+str(current_cmp))
        current_cmp=string_comparison('cgpa float);',command[5])
        if current_cmp!=False:
            l4=len(current_cmp['Missing'])
            que3_mistakes.append("In 6th input box, Characters "+str(current_cmp))
        if (len(que3_mistakes)==0):
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists students")
                mycursor.execute(full_query)
                que3_success_ack.configure(text='Well Done! You got it Right')
                que3_full_query.configure(text='command: create table students(roll int, name varchar(20), year int, cgpa float) ;')
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                que3_full_query.configure(text='')
                que3_success_ack.configure(text='')
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}\n'.format(err.errno, err.sqlstate, err.msg))
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!") 
        else:
            if len(que3_mistakes)==4:
                if (l1==3 or l2==4 or l3==4 or l4==4):
                    que3_full_query.configure(text='')
                    que3_success_ack.configure(text='')
                    messagebox.showerror("Error","Enter the column names as specified in the question")
                    que3_mistakes=[]
                    return
                else:
                    que3_full_query.configure(text='')
                    que3_success_ack.configure(text='')
                    que3_mistakes="\n".join(que3_mistakes)
                    messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}\n'.format(err.errno, err.sqlstate, err.msg)+"\n"+que3_mistakes)
            else:
                que3_full_query.configure(text='')
                que3_success_ack.configure(text='')
                que3_mistakes="\n".join(que3_mistakes)
                messagebox.showerror("Error",'You are unable to get it right\nPlease read the info in "View in Detail"\n'+str(que3_mistakes))
        for_dicts(topic_count,'DDL')   
    elif num==4:
        command=[que4_sol1.get().lower().strip(),que4_sol2.get().lower().strip(),remove_spaces(que4_sol3.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que4_full_query.configure(text='')
            que4_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif 'drop' not in full_query or 'table' not in full_query:
            que4_full_query.configure(text='')
            que4_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - Drop Table [Table_name]\nYou can get the related information by "View in Detail" Button')
        elif command[2]!="students;":
            que4_full_query.configure(text='')
            que4_success_ack.configure(text='')
            messagebox.showerror("Error","Table Not found!\ncheck the name mentioned in the question\nDon't forgot to use semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("create table if not exists students(id int)")
                mycursor.execute(full_query)
                que4_success_ack.configure(text='Well Done! You got it Right')
                que4_full_query.configure(text='command: drop table students ;')
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que4_full_query.configure(text='')
                que4_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!") 
        for_dicts(topic_count,'DDL')
    elif num==5:
        command=[que5_sol1.get().lower().strip(),que5_sol2.get().lower().strip(),que5_sol3.get().lower().strip(),remove_spaces(que5_sol4.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="" or command[3]=="":
            que5_full_query.configure(text='')
            que5_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif 'rename table' not in full_query or 'to' not in full_query:
            que5_full_query.configure(text='')
            que5_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - rename [table_name] to [new_table_name]\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="students":
            que5_full_query.configure(text='')
            que5_success_ack.configure(text='')
            messagebox.showerror("Error","Table to be changed Not found!\ncheck the name mentioned in the question")
        elif command[3]!="students_itdept;":
            que5_full_query.configure(text='')
            que5_success_ack.configure(text='')
            messagebox.showerror("Error","New name should be same as mentioned in the question\nDon't forgot to use semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("create table if not exists students(id int)")
                mycursor.execute("drop table if exists students_itdept")
                mycursor.execute(full_query)
                que5_success_ack.configure(text='Well Done! You got it Right')
                que5_full_query.configure(text='command: rename table students to students_itdept;') 
                for_dicts(crct_count,'DDL')               
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que5_full_query.configure(text='')
                que5_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")  
        for_dicts(topic_count,'DDL')
    elif num==6:   
        def que6_error():
            result=messagebox.askquestion("Error",'You need a practice on creating a table\nPlease refer "4.CREATE TABLE" Topic\n\nError No: {}\nSQL State: {}\n{}\n\nDo you want to go to the "CREATE TABLE" topic?'.format(err.errno, err.sqlstate, err.msg),icon='error')
            if result=="yes":
                open_topic_level1(3)  
            else:
                return     
        command=[que6_sol1.get().lower().strip(),que6_sol2.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="CREATE TABLE STUDENTS ( ID INT           ,".lower() or command[1]=="     VARCHAR(20),      INT,      FLOAT)".lower():
            que6_full_query.configure(text='')
            que6_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")                
        elif "primary key" not in full_query:
            que6_full_query.configure(text='')
            que6_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax for declaring primary key\nYou can see the note at the bottom\nYou can get the related information by "View in Detail" Button')
        else:
            if full_query[-1]!=";" or command[1].count(';')>1:
                que6_full_query.configure(text='')
                que6_success_ack.configure(text='')
                messagebox.showerror("Error","Please use semi-colon at the end of the query\nDon't put any extra characters after the semi-colon it leads to MySQL connection termination")
            else:
                try:
                    mycursor.execute("create database if not exists its")
                    mycursor.execute("use its;")
                    mycursor.execute("drop table if exists students")
                    mycursor.execute(full_query)
                    que6_success_ack.configure(text='Well Done! You got it Right')
                    que6_full_query.configure(text='command: create table students(id int primary key,name varchar(20),year int,cgpa float);')
                    for_dicts(crct_count,'KEYS')
                except mysql.connector.Error as err:
                    que6_error()
                    que6_full_query.configure(text='')
                    que6_success_ack.configure(text='')
                except Exception as e:
                    messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!"+str(e)) 
        for_dicts(topic_count,'KEYS')
    elif num==7:
        command=[]
        for i in range(1,5):
            s=f'command.append(que{num}_sol{i}.get().strip().lower())'
            exec(s) 
        if command[0]=="" or command[1]=="" or command[2]=="" or command[3]=="":
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")
            que7_full_query.configure(text='')
            que7_success_ack.configure(text='')
            return
        full_query=" ".join(command)
        if command[0]!="CREATE TABLE STUDENT_RESULTS(ID INT,NAME VARCHAR(20),SGPA FLOAT,".lower():
            que7_full_query.configure(text='')
            que7_success_ack.configure(text='')
            que7_mistakes1=string_comparison("CREATE TABLE STUDENT_RESULTS(ID INT,NAME VARCHAR(20),SGPA FLOAT,".lower(),command[0])
            if que7_mistakes1!=False:
                messagebox.showerror("Error","error in table creation please do check the query or practice '4.CREATE TABLE' topic and show here\n\nIn 1st input box Characters: "+str(que7_mistakes1)) 
                que7_full_query.configure(text='')
                que7_success_ack.configure(text='')
                return       
        que7_mistakes2=string_comparison("FOREIGN KEY(ID)".lower(),command[1])
        if que7_mistakes2!=False:
                messagebox.showerror("Error","error in table creation please do check the query or practice '4.CREATE TABLE' topic and show here\n\nIn 2nd input box Characters: "+str(que7_mistakes2)) 
                que7_full_query.configure(text='')
                que7_success_ack.configure(text='')
                return
        if "references" not in full_query:
            que7_full_query.configure(text='')
            que7_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax for declaring foreign key\nYou can see the note at the bottom\nYou can get the related information by "View in Detail" Button')
            return
        que7_mistakes4=string_comparison("STUDENTS(ID));".lower(),command[3])
        if que7_mistakes4!=False:
            messagebox.showerror("Error","error in table creation please do check the query or practice '4.CREATE TABLE' topic and show here\n\nIn 4th input box Characters: "+str(que7_mistakes4)) 
            que7_full_query.configure(text='')
            que7_success_ack.configure(text='')
            return
        try:
            mycursor.execute("create database if not exists its")
            mycursor.execute("use its;")
            mycursor.execute("drop table if exists student_results")
            mycursor.execute("drop table if exists students")
            mycursor.execute("create table if not exists students(id int primary key,name varchar(20),year int,cgpa float);")
            mycursor.execute(full_query)
            que7_success_ack.configure(text='Well Done! You got it Right')
            que7_full_query.configure(text='command: create table student_results(id int,name varchar(20),\nsgpa float,foreign key(id) references students(id));')
            for_dicts(crct_count,'KEYS')
        except mysql.connector.Error as err:
            que7_full_query.configure(text='')
            que7_success_ack.configure(text='')
            messagebox.showerror("Error",'You are unable to get it right\nYou might have wrong keywords check the spellings\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
        except:
            messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,'KEYS')
    elif num==8.1:
        command=[que8_1_sol1.get().lower().strip(),que8_1_sol2.get().lower().strip(),que8_1_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que8_1_full_query.configure(text='')
            que8_1_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")           
        elif 'alter' not in full_query or 'add column' not in full_query:
            que8_1_full_query.configure(text='')
            que8_1_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name add column ...\nYou can get the related information by "View in Detail" Button')
        elif command[2]!="percentage float;":
            que8_1_full_query.configure(text='')
            que8_1_success_ack.configure(text='')
            messagebox.showerror("Error","Name & type of the new column should same as mentioned in the question you might forgot to add semi-colon")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists results;")
                mycursor.execute("create table if not exists results(id int)")
                mycursor.execute(full_query)
                que8_1_success_ack.configure(text='Well Done! You got it Right')
                que8_1_full_query.configure(text="command: alter table results add column percentage float ;")
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que8_1_full_query.configure(text='')
                que8_1_success_ack.configure(text='')
        for_dicts(topic_count,'DDL')
    elif num==8.2:
        command=[que8_2_sol1.get().lower().strip(),que8_2_sol2.get().lower().strip(),que8_2_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que8_2_full_query.configure(text='')
            que8_2_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")          
        elif 'alter' not in full_query or 'modify column' not in full_query:
            que8_2_full_query.configure(text='')
            que8_2_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name modify column ...\nYou can get the related information by "View in Detail" Button')
        elif command[2]!="name varchar(40);":
            que8_2_full_query.configure(text='')
            que8_2_success_ack.configure(text='')
            messagebox.showerror("Error","Name & type of the new column should same as mentioned in the question you might forgot to add semi-colon")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists student_results")
                mycursor.execute("drop table if exists students;")
                mycursor.execute("create table if not exists students(name varchar(10))")
                mycursor.execute(full_query)
                que8_2_success_ack.configure(text='Well Done! You got it Right')
                que8_2_full_query.configure(text="command: alter table results modify column name varchar(40);")
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que8_2_full_query.configure(text='')
                que8_2_success_ack.configure(text='') 
        for_dicts(topic_count,'DDL')
    elif num==8.3:
        command=[que8_3_sol1.get().lower().strip(),que8_3_sol2.get().lower().strip(),que8_3_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que8_3_full_query.configure(text='')
            que8_3_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")           
        elif 'alter' not in full_query or 'drop column' not in full_query:
            que8_3_full_query.configure(text='')
            que8_3_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name drop column colname\nYou can get the related information by "View in Detail" Button')
        elif command[2]!="contact;":
            que8_3_full_query.configure(text='')
            que8_3_success_ack.configure(text='')
            que_8_3_mis=string_comparison("contact;",command[2].lower())
            if que_8_3_mis!=False:
                messagebox.showerror("Error","Name column should be same as mentioned in the question\nIn 3rd input box Characters:"+str(que_8_3_mis))
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists student_results")
                mycursor.execute("drop table if exists students")
                mycursor.execute("create table if not exists students(id int, contact int)")
                mycursor.execute(full_query)
                que8_3_success_ack.configure(text='Well Done! You got it Right')
                que8_3_full_query.configure(text="command: alter table students drop column contact;")
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que8_3_full_query.configure(text='')
                que8_3_success_ack.configure(text='')   
        for_dicts(topic_count,'DDL')          
    elif num==8.4:
        command=[que8_4_sol1.get().lower().strip(),que8_4_sol2.get().lower().strip(),que8_4_sol3.get().lower().strip()]
        full_query=" ".join(command)
        print(full_query)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que8_4_full_query.configure(text='')
            que8_4_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")           
        elif 'alter' not in command[0]:
            que8_4_full_query.configure(text='')
            que8_4_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name change column..\nYou can get the related information by "View in Detail" Button')
        elif command[1]!='change column':
            que8_4_full_query.configure(text='')
            que8_4_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name change column..\nYou can get the related information by "View in Detail" Button')
        elif command[2]!="id student_id int;":
            que8_4_full_query.configure(text='')
            que8_4_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - alter table tab_name change column col_name newname datatype\nYou can get the related information by "View in Detail" Button')
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists students")
                mycursor.execute("create table if not exists students(id int)")
                mycursor.execute(full_query)
                que8_4_success_ack.configure(text='Well Done! You got it Right')
                que8_4_full_query.configure(text="command: alter table students change column id student_id int;")
                for_dicts(crct_count,'DDL')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que8_4_full_query.configure(text='')
                que8_4_success_ack.configure(text='') 
        for_dicts(topic_count,'DDL')
    elif num==9:
        command=[que9_sol1.get().lower().strip(),que9_sol2.get().lower().strip(),que9_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que9_full_query.configure(text='')
            que9_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")
            return     
        elif command[1]!='avengers' :
            que9_full_query.configure(text='')
            que9_success_ack.configure(text='')
            messagebox.showerror("Error",'Table should be same as mentioned in the question')
            return
        elif command[2]=="VALUES(                 ,                  ,                );".lower().strip():
            que9_full_query.configure(text='')
            que9_success_ack.configure(text='')
            messagebox.showerror("Error",'Please enter the data as specified in the question')
            return
        que9_mis1=string_comparison('values(3000,"ironman",1);',command[2])
        if que9_mis1=={'Extra': ["'"], 'Missing': ['"']}:
            que9_full_query.configure(text='')
            que9_success_ack.configure(text='')            
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists avengers")
                mycursor.execute("create table if not exists avengers(id int,name varchar(30),ranked int)")
                mycursor.execute(full_query)
                que9_success_ack.configure(text='Well Done! You got it Right')
                que9_full_query.configure(text="command: insert into avengers(3000,'ironman',1);")
                for_dicts(crct_count,'DML')
                return
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters or wrong syntax\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que9_full_query.configure(text='')
                que9_success_ack.configure(text='')
                return
        if que9_mis1!=False:
            que9_full_query.configure(text='')
            que9_success_ack.configure(text='')            
            messagebox.showerror("Error","Kindly check the data to be inserted with the data your enetered\nThe data order should match with the column order!\nIn the 3rd Input box Characters:"+str(que9_mis1))
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists avengers")
                mycursor.execute("create table if not exists avengers(id int,name varchar(30),ranked int)")
                mycursor.execute(full_query)
                que9_success_ack.configure(text='Well Done! You got it Right')
                que9_full_query.configure(text='command: insert into avengers(3000,"ironman",1);')
                for_dicts(crct_count,'DML')
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters or wrong syntax\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que9_full_query.configure(text='')
                que9_success_ack.configure(text='')
        for_dicts(topic_count,'DML')
    elif num==10:
        command=[que10_sol1.get().lower().strip(),que10_sol2.get().lower().strip(),que10_sol3.get().lower().strip(),que10_sol4.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="" or command[3]=="":
            que10_full_query.configure(text='')
            que10_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")            
        elif 'delete from' not in full_query or 'where' not in full_query:
            que10_full_query.configure(text='')
            que10_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - delete from [table_name] where [condition]\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="avengers":
            que10_full_query.configure(text='')
            que10_success_ack.configure(text='')
            messagebox.showerror("Error","Table name should be same as mentioned in the question!")
        elif "ranked" not in full_query or "=" not in full_query or "1" not in full_query:
            que10_full_query.configure(text='')
            que10_success_ack.configure(text='')
            messagebox.showerror("Error","Check the condition properly\nYou need to mention the column that gives the rank of the Avenger")
        elif full_query[-1]!=';' or command[3].count(";")>1:
            messagebox.showerror("Error","You might have enteres extra characters or forgot to use semi-colon")
        else:
            que10_mis1=remove_spaces(command[3])
            if len(que10_mis1)>9:
                que10_full_query.configure(text='')
                que10_success_ack.configure(text='')
                messagebox.showerror("Error","MySQL wont throws an error upon trying to do deletion of an unpresent data\nkindly check the condition in your query")
                return
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("create table if not exists avengers(id int,name varchar(30),ranked int);")
                mycursor.execute("insert into avengers values(3000,'ironman',1)")
                mycursor.execute(full_query)
                que10_success_ack.configure(text='Well Done! You got it Right')
                que10_full_query.configure(text='command: delete from avengers where ranked=1;')  
                for_dicts(crct_count,'DML')              
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que10_full_query.configure(text='')
                que10_success_ack.configure(text='')     
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")   
        for_dicts(topic_count,'DML')   
    elif num==11:
        command=[que11_sol1.get().lower().strip(),que11_sol2.get().lower().strip(),que11_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que11_full_query.configure(text='')
            que11_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")     
            return       
        if command[0]!='update avengers':
            que11_full_query.configure(text='')
            que11_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - update [table_name] set colname=[data] where [condition]\nYou can get the related information by "View in Detail" Button')
            return  
        que11_mis=string_comparison("set id = 1",command[1])
        if que11_mis!=False:
            que11_full_query.configure(text='')
            que11_success_ack.configure(text='')
            messagebox.showerror("Error","You need to specify column name and data to updated as specified in the question\nOr you can have a look at the syntax\nIn the 2nd Input Box Characters:"+str(que11_mis))    
            return 
        que11_mis=string_comparison("where id = 3000;",command[2])
        if que11_mis!=False:
            que11_full_query.configure(text='')
            que11_success_ack.configure(text='')
            messagebox.showerror("Error","You need to specify column name and data to updated as specified in the question\nOr you can have a look at the syntax\nIn the 2nd Input Box Characters:"+str(que11_mis))
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("create table if not exists avengers(id int,name varchar(30),ranked int);")
                mycursor.execute("insert into avengers values(3000,'ironman',1)")
                mycursor.execute(full_query)
                que11_success_ack.configure(text='Well Done! You got it Right')
                que11_full_query.configure(text='command: update avengers set id = 1 where id = 3000;')
                for_dicts(crct_count,'DML')                   
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nCheck the syntax properly\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que11_full_query.configure(text='')
                que11_success_ack.configure(text='')     
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")    
        for_dicts(topic_count,'DML')   
    elif num==13:
        command=[que13_sol1.get().lower().strip(),remove_spaces(que13_sol2.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="":
            que13_full_query.configure(text='')
            que13_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!='show':
            que13_full_query.configure(text='')
            que13_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[1]!='tables;':
            que13_full_query.configure(text='')
            que13_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nDont forgot to use semi-colon at the end of the query\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        else:
            try:
                mycursor.execute("create database if not exists its;")
                mycursor.execute("use its;")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que13_success_ack.configure(text='Well Done! You got it Right')
                que13_full_query.configure(text='command: show tables ;') 
                for_dicts(crct_count,"DDL")  
            except mysql.connector.Error as err:
                que13_full_query.configure(text='')
                que13_success_ack.configure(text='')
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!") 
        for_dicts(topic_count,"DDL")
    elif num==14:
        command=[que14_sol1.get().lower().strip(),que14_sol2.get().lower().strip(),remove_spaces(que14_sol3.get().lower().strip())]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que14_full_query.configure(text='')
            que14_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")            
        elif command[0]!="select * from employees":
            que14_full_query.configure(text='')
            que14_success_ack.configure(text='')
            messagebox.showerror("Error","In input box 1 Please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[1]!="where":
            que14_full_query.configure(text='')
            que14_success_ack.configure(text='')
            messagebox.showerror("Error","In input box 2 Please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[2]!="empid=120;":
            que14_full_query.configure(text='')
            que14_success_ack.configure(text='')
            messagebox.showerror("Error","give the columnname & Value properly or\nDon't forgot to use semi-colon")
        else:
            try:
                mycursor.execute("create database if not exists its;")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int)")
                mycursor.execute("insert into employees values(120),(155);")
                mydb.commit()
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que14_success_ack.configure(text='Well Done! You got it Right')
                que14_full_query.configure(text='command: select * from employees where empid=120 ;')  
                for_dicts(crct_count,"CLAUSES")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que14_full_query.configure(text='')
                que14_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"CLAUSES")
    elif num==15:
        command=[que15_sol1.get().lower().strip(),que15_sol2.get().lower().strip(),que15_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que15_full_query.configure(text='')
            que15_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")            
        elif "distinct" not in command[0] or "select" not in command[0]:
            que15_full_query.configure(text='')
            que15_success_ack.configure(text='')
            messagebox.showerror("Error","In input box 1 you have to use 'DISTINCT' keyword with 'SELECT'\nYou can get the related information by 'View in Detail' Button")
        elif command[1]!="salary":
            que15_full_query.configure(text='')
            que15_success_ack.configure(text='')
            messagebox.showerror("Error","In input box 2 Please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        elif command[2]!="from employees;":
            que15_full_query.configure(text='')
            que15_success_ack.configure(text='')
            messagebox.showerror("Error","give the columnname & Value properly or\nDon't forgot to use semi-colon")
        else:
            try:
                mycursor.execute("create database if not exists its;")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(salary float)")
                mycursor.execute("insert into employees values(40000),(50000),(40000);")
                mydb.commit()
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que15_success_ack.configure(text='Well Done! You got it Right')
                que15_full_query.configure(text='command: select distinct salary from employees;')
                for_dicts(crct_count,"CLAUSES")  
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You might have entered extra characters\nYou are unable to get it right\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que15_full_query.configure(text='')
                que15_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"CLAUSES")
    elif num==16:
        command=[que16_sol1.get().lower().strip(),que16_sol2.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="":
            que16_full_query.configure(text='')
            que16_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif "order" not in full_query or "by" not in full_query or "salary" not in full_query:
            que16_full_query.configure(text='')
            que16_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\ngive the column name to order the data in the table correctly or\ncheck the syntax properly")
        elif ";" not in full_query and full_query.count(";"):
            que16_full_query.configure(text='')
            que16_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nDont forgot to use semi-colon at the end of the query\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        else:
            try:
                mycursor.execute("create database if not exists its;")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mydb.commit()
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que16_success_ack.configure(text='Well Done! You got it Right')
                que16_full_query.configure(text='command: select * from employees order by salary;') 
                for_dicts(crct_count,"CLAUSES")  
            except mysql.connector.Error as err:
                que16_full_query.configure(text='')
                que16_success_ack.configure(text='')
                result=messagebox.askquestion("?",'Error No: {}\nSQL State: {}\n{}\n\nYou need to practise SELECT clause do you want to go to SELECT clause?'.format(err.errno, err.sqlstate, err.msg))
                if result=="yes":
                    open_topic_level1(12)                       
                else:
                    return
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"CLAUSES")
    elif num==17:
        command=[que17_sol1.get().lower().strip(),que17_sol2.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="":
            que17_full_query.configure(text='')
            que17_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif "group" not in full_query or "by" not in full_query or "department" not in full_query:
            que17_full_query.configure(text='')
            que17_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\ngive the column name to order the data in the table correctly or\ncheck the syntax properly")
        elif ";" not in full_query and full_query.count(";"):
            que17_full_query.configure(text='')
            que17_success_ack.configure(text='')
            messagebox.showerror("Error","You are doing good!\nDont forgot to use semi-colon at the end of the query\nBut please check the spellings & syntax properly\nYou can get the related information by 'View in Detail' Button")
        else:
            try:
                mycursor.execute("create database if not exists its;")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mydb.commit()
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que17_success_ack.configure(text='Well Done! You got it Right')
                que17_full_query.configure(text='command: select * from employees group by department;')   
                for_dicts(crct_count,"CLAUSES")
            except mysql.connector.Error as err:
                que17_full_query.configure(text='')
                que17_success_ack.configure(text='')
                result=messagebox.askquestion("?",'Error No: {}\nSQL State: {}\n{}\n\nYou need to practise SELECT clause do you want to go to SELECT clause?'.format(err.errno, err.sqlstate, err.msg))
                if result=="yes":
                    open_topic_level1(12)                       
                else:
                    return
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"CLAUSES")
    elif num==19:
        command=[que19_sol1.get().lower().strip(),que19_sol2.get().lower().strip(),que19_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que19_full_query.configure(text='')
            que19_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!="select":
            que19_full_query.configure(text='')
            que19_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="count(*)":
            que19_full_query.configure(text='')
            que19_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif "from" not in command[2] or "employees" not in command[2]:
            que19_full_query.configure(text='')
            que19_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif ";" not in command[2] or full_query.count(";")>1:
            que19_full_query.configure(text='')
            que19_success_ack.configure(text='')
            messagebox.showerror("Error","Dont forgot to use Semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("create table if not exists employees(id int)")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que19_success_ack.configure(text='Well Done! You got it Right')
                que19_full_query.configure(text='command: select count(*) from employees;')
                for_dicts(crct_count,"Agg Functions")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que19_full_query.configure(text='')
                que19_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"Agg Functions")
    elif num==20:
        command=[que20_sol1.get().lower().strip(),que20_sol2.get().lower().strip(),que20_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que20_full_query.configure(text='')
            que20_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!="select":
            que20_full_query.configure(text='')
            que20_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="sum(salary)":
            que20_full_query.configure(text='')
            que20_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nSpecify the column name properly in the parenthesis\nYou can get the related information by "View in Detail" Button')
        elif "from" not in command[2] or "employees" not in command[2]:
            que20_full_query.configure(text='')
            que20_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif ";" not in command[2] or full_query.count(";")>1:
            que20_full_query.configure(text='')
            que20_success_ack.configure(text='')
            messagebox.showerror("Error","Dont forgot to use Semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que20_success_ack.configure(text='Well Done! You got it Right')
                que20_full_query.configure(text='command: select sum(salary) from employees;')
                for_dicts(crct_count,"Agg Functions")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que20_full_query.configure(text='')
                que20_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"Agg Functions")
    elif num==21:
        command=[que21_sol1.get().lower().strip(),que21_sol2.get().lower().strip(),que21_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que21_full_query.configure(text='')
            que21_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!="select":
            que21_full_query.configure(text='')
            que21_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="max(salary)":
            que21_full_query.configure(text='')
            que21_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nSpecify the column name properly in the parenthesis\nYou can get the related information by "View in Detail" Button')
        elif "from" not in command[2] or "employees" not in command[2]:
            que21_full_query.configure(text='')
            que21_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif ";" not in command[2] or full_query.count(";")>1:
            que21_full_query.configure(text='')
            que21_success_ack.configure(text='')
            messagebox.showerror("Error","Dont forgot to use Semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que21_success_ack.configure(text='Well Done! You got it Right')
                que21_full_query.configure(text='command: select max(salary) from employees;')
                for_dicts(crct_count,"Agg Functions")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que21_full_query.configure(text='')
                que21_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"Agg Functions")
    elif num==22:
        command=[que22_sol1.get().lower().strip(),que22_sol2.get().lower().strip(),que22_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que22_full_query.configure(text='')
            que22_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!="select":
            que22_full_query.configure(text='')
            que22_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="min(salary)":
            que22_full_query.configure(text='')
            que22_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nSpecify the column name properly in the parenthesis\nYou can get the related information by "View in Detail" Button')
        elif "from" not in command[2] or "employees" not in command[2]:
            que22_full_query.configure(text='')
            que22_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif ";" not in command[2] or full_query.count(";")>1:
            que22_full_query.configure(text='')
            que22_success_ack.configure(text='')
            messagebox.showerror("Error","Dont forgot to use Semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que22_success_ack.configure(text='Well Done! You got it Right')
                que22_full_query.configure(text='command: select min(salary) from employees;')
                for_dicts(crct_count,"Agg Functions")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que22_full_query.configure(text='')
                que22_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"Agg Functions")
    elif num==23:
        command=[que23_sol1.get().lower().strip(),que23_sol2.get().lower().strip(),que23_sol3.get().lower().strip()]
        full_query=" ".join(command)
        if command[0]=="" or command[1]=="" or command[2]=="":
            que23_full_query.configure(text='')
            que23_success_ack.configure(text='')
            messagebox.showerror("Error","Please do enter the query in the allocated boxes without leaving any, this is for your understanding")    
        elif command[0]!="select":
            que23_full_query.configure(text='')
            que23_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif command[1]!="avg(salary)":
            que23_full_query.configure(text='')
            que23_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nSpecify the column name properly in the parenthesis\nYou can get the related information by "View in Detail" Button')
        elif "from" not in command[2] or "employees" not in command[2]:
            que23_full_query.configure(text='')
            que23_success_ack.configure(text='')
            messagebox.showerror("Error",'Check the syntax - select AGG-FUNC from Tab_name\nYou can get the related information by "View in Detail" Button')
        elif ";" not in command[2] or full_query.count(";")>1:
            que23_full_query.configure(text='')
            que23_success_ack.configure(text='')
            messagebox.showerror("Error","Dont forgot to use Semi-colon at the end of the query")
        else:
            try:
                mycursor.execute("create database if not exists its")
                mycursor.execute("use its;")
                mycursor.execute("drop table if exists employees")
                mycursor.execute("create table if not exists employees(empid int, name varchar(10),salary float,department varchar(10))")
                mycursor.execute("insert into employees values(1,'a',40000,'it'),(2,'b',40000,'it'),(3,'c',60000,'csit');")
                mycursor.execute(full_query)
                l=mycursor.fetchall()
                que23_success_ack.configure(text='Well Done! You got it Right')
                que23_full_query.configure(text='command: select avg(salary) from employees;')
                for_dicts(crct_count,"Agg Functions")
            except mysql.connector.Error as err:
                messagebox.showerror("Error",'You are unable to get it right\nYou might have entered extra characters\n\nError No: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))
                que23_full_query.configure(text='')
                que23_success_ack.configure(text='')
            except:
                messagebox.showwarning("Warning","If any malfunction found please restart the application\nkindly forgive us we will work on this issue!")
        for_dicts(topic_count,"Agg Functions")
    else:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def Reset(num):
    if num==0:
        que0_sol1.set("CREATE")
        que0_sol2.set("")
        que0_sol3.set("")
        que0_full_query.configure(text='')
        que0_success_ack.configure(text='')
    elif num==1:
        que1_sol1.set("DROP")
        que1_sol2.set("")
        que1_sol3.set("")
        que1_full_query.configure(text='')
        que1_success_ack.configure(text='')
    elif num==2:
        que2_sol1.set("")
        que2_sol2.set("DATABASES;")
        que2_full_query.configure(text='')
        que2_success_ack.configure(text='')
    elif num==3:
        que3_sol1.set("CREATE TABLE")
        que3_sol2.set("")
        que3_sol3.set(" (        INT,")
        que3_sol4.set("        VARCHAR(20),")
        que3_sol5.set("        INT,")
        que3_sol6.set("        FLOAT);")
        que3_full_query.configure(text='')
        que3_success_ack.configure(text='')
    elif num==4:
        que4_sol1.set("DROP")
        que4_sol2.set("")
        que4_sol3.set("")
        que4_full_query.configure(text='')
        que4_success_ack.configure(text='')
    elif num==5:
        que5_sol1.set("RENAME TABLE")
        que5_sol2.set("")
        que5_sol3.set("TO")
        que5_sol4.set("")
        que5_full_query.configure(text='')
        que5_success_ack.configure(text='')
    elif num==6:
        que6_sol1.set("CREATE TABLE STUDENTS ( ID INT           ,")
        que6_sol2.set("     VARCHAR(20),      INT,      FLOAT);")
        que6_full_query.configure(text='')
        que6_success_ack.configure(text='')
    elif num==7:
        que7_sol1.set("CREATE TABLE STUDENT_RESULTS(ID INT,NAME VARCHAR(20),SGPA FLOAT,")
        que7_sol2.set("")
        que7_sol3.set("REFERENCES")
        que7_sol4.set("")
        que7_full_query.configure(text='')
        que7_success_ack.configure(text='')
    elif num==8.1:
        que8_1_sol1.set("                TABLE RESULTS")
        que8_1_sol2.set("")
        que8_1_sol3.set("PERCENTAGE FLOAT;")
        que8_1_full_query.configure(text='')
        que8_1_success_ack.configure(text='')
    elif num==8.2:
        que8_2_sol1.set("       TABLE STUDENTS")
        que8_2_sol2.set("")
        que8_2_sol3.set("NAME VARCHAR(40);")
        que8_2_full_query.configure(text='')
        que8_2_success_ack.configure(text='')
    elif num==8.3:
        que8_3_sol1.set("       TABLE STUDENTS")
        que8_3_sol2.set("")
        que8_3_sol3.set("CONTACT;")
        que8_3_full_query.configure(text='')
        que8_3_success_ack.configure(text='')
    elif num==8.4:
        que8_4_sol1.set("       TABLE STUDENTS")
        que8_4_sol2.set("")
        que8_4_sol3.set("ID STUDENT_ID INT;")
        que8_4_full_query.configure(text='')
        que8_4_success_ack.configure(text='')
    elif num==9:
        que9_sol1.set("INSERT INTO")
        que9_sol2.set("")
        que9_sol3.set("VALUES(                 ,                  ,                );")
        que9_full_query.configure(text='')
        que9_success_ack.configure(text='')
    elif num==10:
        que10_sol1.set("DELETE FROM")
        que10_sol2.set("")
        que10_sol3.set("WHERE")
        que10_sol4.set("")
        que10_full_query.configure(text='')
        que10_success_ack.configure(text='')
    elif num==11:
        que11_sol1.set("UPDATE AVENGERS")
        que11_sol2.set("SET")
        que11_sol3.set("WHERE")
        que11_full_query.configure(text='')
        que11_success_ack.configure(text='')
    elif num==13:
        que13_sol1.set("")
        que13_sol2.set("TABLES;")
        que13_full_query.configure(text='')
        que13_success_ack.configure(text='')
    elif num==14:
        que14_sol1.set("SELECT * FROM EMPLOYEES")
        que14_sol2.set("")
        que14_sol3.set("EMPID=")
        que14_full_query.configure(text='')
        que14_success_ack.configure(text='')
    elif num==15:
        que15_sol1.set("SELECT")
        que15_sol2.set("SALARY")
        que15_sol3.set("FROM EMPLOYEES;")
        que15_full_query.configure(text='')
        que15_success_ack.configure(text='')
    elif num==16:
        que16_sol1.set("")
        que16_sol2.set("ORDER BY    ;")
        que16_full_query.configure(text='')
        que16_success_ack.configure(text='')
    elif num==17:
        que17_sol1.set("")
        que17_sol2.set("GROUP BY    ;")
        que17_full_query.configure(text='')
        que17_success_ack.configure(text='')
    elif num==19:
        que19_sol1.set("SELECT")
        que19_sol2.set("")
        que19_sol3.set("FROM EMPLOYEES;")
        que19_full_query.configure(text='')
        que19_success_ack.configure(text='')
    elif num==20:
        que20_sol1.set("SELECT")
        que20_sol2.set("")
        que20_sol3.set("FROM EMPLOYEES;")
        que20_full_query.configure(text='')
        que20_success_ack.configure(text='')
    elif num==21:
        que21_sol1.set("SELECT")
        que21_sol2.set("")
        que21_sol3.set("FROM EMPLOYEES;")
        que21_full_query.configure(text='')
        que21_success_ack.configure(text='')
    elif num==22:
        que22_sol1.set("SELECT")
        que22_sol2.set("")
        que22_sol3.set("FROM EMPLOYEES;")
        que22_full_query.configure(text='')
        que22_success_ack.configure(text='')
    elif num==23:
        que23_sol1.set("SELECT")
        que23_sol2.set("")
        que23_sol3.set("FROM EMPLOYEES;")
        que23_full_query.configure(text='')
        que23_success_ack.configure(text='')
    else:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def View_solution(num):
    if num==0:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que0_full_query.configure(text="command: create database tutoringsystem;")
        else:
            return   
    elif num==1:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que1_full_query.configure(text="command: drop database tutoringsystem;")
        else:
            return   
    elif num==2:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que2_full_query.configure(text='command: show databases ;')   
        else:
            return
    elif num==3:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que3_full_query.configure(text='command: create table students(roll int, name varchar(20), year int, cgpa float) ;')
        else:
            return
    elif num==4:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que4_full_query.configure(text='command: drop table students ;')
        else:
            return
    elif num==5:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que5_full_query.configure(text='command: rename table students to students_itdept;')
        else:
            return
    elif num==6:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que6_full_query.configure(text='command: create table students(id int primary key,name varchar(20),year int,cgpa float);')            
        else:
            return 
    elif num==7:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que7_full_query.configure(text='command: create table student_results(id int,name varchar(20),\nsgpa float,foreign key(id) references students(id));')
        else:
            return
    elif num==9:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que9_full_query.configure(text="command: insert into avengers(3000,'ironman',1);")    
        else:
            return
    elif num==10:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que10_full_query.configure(text='command: delete from avengers where ranked=1;')     
        else:
            return
    elif num==11:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que11_full_query.configure(text='command: update avengers set id = 1 where id = 3000;')             
        else:
            return
    elif num==13:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que13_full_query.configure(text='command: show tables ;')                         
        else:
            return
    elif num==14:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que14_full_query.configure(text='command: select * from employees where empid=120 ;')                         
        else:
            return 
    elif num==15:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que15_full_query.configure(text='command: select distinct salary from employees;')                        
        else:
            return
    elif num==16:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que16_full_query.configure(text='command: select * from employees order by salary;')                        
        else:
            return
    elif num==17:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que17_full_query.configure(text='command: select * from employees group by department;')                                  
        else:
            return
    elif num==19:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que19_full_query.configure(text='command: select count(*) from employees;')                                  
        else:
            return
    elif num==20:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que20_full_query.configure(text='command: select sum(salary) from employees;')                                  
        else:
            return
    elif num==21:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que21_full_query.configure(text='command: select max(salary) from employees;')                                  
        else:
            return
    elif num==22:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que22_full_query.configure(text='command: select min(salary) from employees;')                                  
        else:
            return
    elif num==23:
        result=messagebox.askquestion("?",'Do you really want to see the solution')
        if result=="yes":
            que23_full_query.configure(text='command: select avg(salary) from employees;')                                  
        else:
            return
    else:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

root=Tk()
try:
    root.iconbitmap(r"itsmysqlicon.ico")
except:
    messagebox.showerror("ICON DELETED!","Application's Icon has been Deleted,You can use without the icon or to have smooth working kindly download the archive again!")
root.title("MySQL Tutor")
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

time_frame=Frame(root,bg='#212121',bd=5,relief='sunken')
time_frame.grid(row=0,column=0, columnspan=1, sticky='nsew')
now = Label(time_frame,font=('Arial 18 bold'),background='#212121',foreground='#5b83ba',padx=20)
time()
date = Label(time_frame,text=f"{dt.datetime.now():%a, %b %d %Y}",font=('Arial 18 bold'),background='#212121',foreground='#5b83ba',padx=20)
date.pack(side=LEFT)
now.pack(side=RIGHT)
main_frame = Frame(root,bg='#212121')
main_frame.grid_columnconfigure(0,weight=1)
main_frame.grid_columnconfigure(1,weight=1)
main_frame.grid_rowconfigure(0,weight=1)
main_frame.grid_rowconfigure(1,weight=1)
main_frame.grid(row=1,column=0,sticky='nsew')
intro_text="""
Hello!\n 
Here's what is this Application for : )\n                                         
Every student who wanted to learn a MySQL language faces difficulty to understand & write proper syntax\n
which is time taking because of un-proper tutoring. We have taken this project to make  beginners\n
free from fear and misconceptions. Our application takes the errors made by the user & performs\n
analysis based on the output or error produced after their compilation and prepares resourceful\n
feedback. It makes users learn from their mistakes effectively. In addition to this, our\n
system lets the user write a command by dividing it into parts, and thereby the user gets a clear\n
idea. There will be few lists of tasks assigned to them to perform execution in the query language.\n
We had faced similar problems when we were beginners to the query language and learning MySQL.\n
We had taken a survey from the group of people who were willing to learn MySQL, the conclusions are\n
Major problem faced by them was knowing right syntax, it is the most important thing. Many people can't\n
able to understand MySQL generated error. Every student who tries to learn a MySQL language face\n
difficulty to understand and write proper syntax which is time taking because of un-proper tutoring.\n
Our team decided to develop a system to overcome the problems that many beginners faced in learning\n
Query language using MySQL.
"""
intro_frame = Frame(main_frame,bg='#212121',bd=5,relief='sunken',padx=10)
intro_frame.grid(row = 0,column=0,sticky='nsew',rowspan=2)
intro_label = Label(intro_frame,text=intro_text,font=('Arial 12'),padx=10,background='#212121', foreground='White',justify='left')
intro_label.grid(row=0,column=0)
connection_frame = Frame(main_frame, bg='#212121',bd=5,relief='sunken', pady = 10)
connection_frame.grid(row=1,column=1,sticky='nsew')

connection_frame.grid_rowconfigure(0,weight=1)
connection_frame.grid_rowconfigure(1,weight=1)
connection_frame.grid_rowconfigure(2,weight=1)
connection_frame.grid_columnconfigure(0,weight=1)
connection_frame.grid_columnconfigure(1,weight=1)
connection_frame.grid_columnconfigure(2,weight=1)

username = StringVar()
password = StringVar()
user_label = Label(connection_frame,text="Username",font=('Arial 13 bold'),background='#212121', foreground='White').grid(row = 0,column = 0)
user_label_none = Label(connection_frame,text=":",font=('Arial 13 bold'),background='#212121', foreground='White').grid(row = 0,column = 1)
ttk.Entry(connection_frame,font=('Arial 12 bold'),width=15,textvariable=username).grid(row=0,column=2)
username.set('root')
pwd_label = Label(connection_frame,text="Password",font=('Arial 13 bold'),background='#212121', foreground='White').grid(row=1,column=0)
pwd_label_none = Label(connection_frame,text=":",font=('Arial 13 bold'),background='#212121', foreground='White').grid(row=1,column=1)
ttk.Entry(connection_frame,font=('Arial 12 bold'),width=15,textvariable=password).grid(row=1,column=2)
connect_btn = Button(connection_frame,bg='green',text="Connect",font=('Arial 12 bold'),height=1,width = 12,command = connect,cursor= "hand2").grid(row=2,column=1)

ui_next_frame = Frame(main_frame, bg='#212121',bd=5,relief='sunken', pady = 10)
ui_next_frame.grid_rowconfigure(0,weight=1)
ui_next_frame.grid_rowconfigure(1,weight=1)
ui_next_frame.grid_rowconfigure(2,weight=1)
ui_next_frame.grid_columnconfigure(0,weight=1)
ui_next_frame.grid_columnconfigure(1,weight=1)
ui_next_frame.grid_columnconfigure(2,weight=1)
ui_frame_label = Label(ui_next_frame,text="Start Learning",font=('Arial 14 bold')).grid(row=0,column=0,sticky='ew',columnspan=3)
ui_btn1 = Button(ui_next_frame,text = "Level  I",bg='#5b83ba',font="Arial 13 bold",height=1,width = 20, command = ui1_frame,cursor= "hand2").grid(row=1,column=1)
ui_btn2 = Button(ui_next_frame,text = "Level  II",bg='#5b83ba',font="Arial 13 bold",height=1,width = 20, command=ui2_frame,cursor= "hand2").grid(row=2,column=1)

connection_desc_frame = Frame(main_frame, bg='#212121',bd=5,relief='sunken', pady = 10)
connection_desc_frame.grid_rowconfigure(0,weight=1)
connection_desc_frame.grid_rowconfigure(1,weight=1)
connection_desc_frame.grid_rowconfigure(2,weight=1)
connection_desc_frame.grid_columnconfigure(0,weight=1)
connection_desc_frame.grid_columnconfigure(1,weight=1)
connection_desc_frame_text="You need to have MySQL tool in your machine,\n\nto connect please enter your MySQL credentials"
Label(connection_desc_frame,text=connection_desc_frame_text,font=('Arial 12 bold')).grid(row=0,column=0,sticky='ew',columnspan=2)
Label(connection_desc_frame,text="To Download ",font=('Arial 12 bold')).grid(row=1,column=0,sticky='ew')
Label(connection_desc_frame,text="To Know how to setup ",font=('Arial 12 bold')).grid(row=2,column=0,sticky='ew')
Button(connection_desc_frame,text = "Here",bg='#5b83ba',font="Arial 12 bold", width = 10,cursor= "hand2", command = lambda : view_in_detail(24)).grid(row=1,column=1,padx=20)
Button(connection_desc_frame,text = "Here",bg='#5b83ba',font="Arial 12 bold", width = 10,cursor= "hand2", command = lambda : view_in_detail(25)).grid(row=2,column=1,padx=20)
connection_desc_frame.grid(row=0,column=1,sticky='nsew',columnspan=2)

ui_frame_level1 = Frame(root,bg='#212121',relief='sunken')
ui_frame_level1.grid_rowconfigure(0,weight=1)
ui_frame_level1.grid_rowconfigure(1,weight=1)
ui_frame_level1.grid_rowconfigure(2,weight=1)
ui_frame_level1.grid_rowconfigure(3,weight=1)
ui_frame_level1.grid_rowconfigure(4,weight=1)
ui_frame_level1.grid_rowconfigure(5,weight=1)
ui_frame_level1.grid_rowconfigure(6,weight=1)
ui_frame_level1.grid_rowconfigure(7,weight=1)
ui_frame_level1.grid_rowconfigure(8,weight=1)
ui_frame_level1.grid_columnconfigure(0,weight=1)
ui_frame_level1.grid_columnconfigure(1,weight=1)
ui_frame_level1.grid_columnconfigure(2,weight=1)

ui_frame_l1buttonslist=Frame(ui_frame_level1,bg='#212121',bd=5,relief='sunken')
ui_frame_l1bottom=Frame(ui_frame_level1,bg='#212121',bd=5,relief='sunken')
ui_frame_l1bottom.grid(row=8,column=0,columnspan=2,sticky="nsew")
ui_frame_l1bottom.grid_rowconfigure(0,weight=1)
ui_frame_l1bottom.grid_rowconfigure(1,weight=1)
ui_frame_l1bottom.grid_columnconfigure(0,weight=1)
ui_frame_l1bottom.grid_columnconfigure(1,weight=1)
ui_frame_l1bottom.grid_columnconfigure(2,weight=1)
ui_l1_bottom_prevq = Button(ui_frame_l1bottom,text = "Previous Topic",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command = ui_frame_prevtopic).grid(row=0,column=0)
ui_l1_bottom_nextq = Button(ui_frame_l1bottom,text = "Next Topic",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command = ui_frame_nexttopic).grid(row=0,column=1)
ui_frame_l1homebutton = Button(ui_frame_l1bottom,text = "Home",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command = home).grid(row=0,column=2)
ui_l1_bottom_nextq = Button(ui_frame_l1bottom,text = "View Performance",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command = performance_graphs).grid(row=1,column=1)

ui1l1_canvas = Canvas(ui_frame_l1buttonslist,width=20,relief='sunken')
ui1l1_canvas.pack(side=LEFT,fill="both",expand="yes")
ui1l1_scrollbar=ttk.Scrollbar(ui_frame_l1buttonslist,orient="vertical",cursor= "hand2",command=ui1l1_canvas.yview)
ui1l1_scrollbar.pack(side=RIGHT,fill="y")
style=ttk.Style()
style.theme_use('classic')
style.configure("Vertical.TScrollbar",background="#5b83ba",troughcolor="#212121")
ui1l1_canvas.configure(yscrollcommand=ui1l1_scrollbar.set)
ui1l1_canvas.bind('<Configure>', lambda e:ui1l1_canvas.configure(scrollregion = ui1l1_canvas.bbox('all')))
ui1l1_listframe=Frame(ui1l1_canvas)
ui1l1_canvas.create_window((0,0), window = ui1l1_listframe)
ui_frame_l1buttonslist.grid(row=0,column=2,rowspan=9,sticky="nsew")
topics_list_ui1=["Create Database","Drop Database","Show Databases","Create Table","Drop Table","Rename Table","Primary Key","Foreign Key","Alter Table","Insertion","Deletion","Updation","Select","Show Tables","Where Clause","Distinct","Order By","Group By","Having","Count()","Sum()","Max()","Min()","Avg()"]

Button(ui1l1_listframe,text="1.Create Database",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(0)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="2.Drop Database",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(1)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="3.Show Databases",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(2)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="4.Create Table",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(3)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="5.Drop Table",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(4)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="6.Rename Table",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(5)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="7.Primary Key",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(6)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="8.Foreign Key",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(7)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="9.Alter Table",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(8)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="10.Insertion",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(9)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="11.Deletion",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(10)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="12.Updation",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(11)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="13.Select",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(12)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="14.Show Tables",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(13)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="15.Where Clause",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(14)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="16.Distinct",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(15)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="17.Order By",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(16)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="18.Group By",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(17)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="19.Having",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(18)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="20.Count()",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(19)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="21.Sum()",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(20)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="22.Max()",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(21)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="23.Min()",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(22)).pack(padx=40,pady=15)
Button(ui1l1_listframe,text="24.Avg()",font="Arial 13 bold",bg="Grey",activeforeground="white",activebackground = "#212121",bd=2,width = 17,cursor= "hand2",command=lambda : open_topic_level1(23)).pack(padx=40,pady=15)

default_Que=Frame(ui_frame_level1,bg='#212121',bd=5,relief='sunken')
default_Que_Label= Label(default_Que,text="Please select a topic\non your Right",font=('Arial 14 bold')).pack()
default_Que.grid(column=0,columnspan=2,row=0,rowspan=8,sticky='nsew')

que0=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que0.grid_propagate(False) 
que0.grid_columnconfigure(0,weight=1)
que0.grid_columnconfigure(1,weight=1)
que0.grid_rowconfigure(0,weight=1)
que0.grid_rowconfigure(1,weight=1)
que0.grid_rowconfigure(2,weight=1)
que0.grid_rowconfigure(3,weight=1)
que0.grid_rowconfigure(4,weight=1)
que0.grid_rowconfigure(5,weight=1)
que0.grid_rowconfigure(6,weight=1)
que0.grid_rowconfigure(7,weight=1)
que0_header_frame=Frame(que0,bg='#212121',bd=5,relief='sunken') 
Label(que0_header_frame,text=topics_list_ui1[0],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que0_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(0)).pack(side=RIGHT,padx=30)
que0_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que0_prblm_text='''Q: Create a database with name "TUTORINGSYSTEM"'''
que0_prblm=Label(que0,text=que0_prblm_text,font=('Arial 12 bold'),padx=20)
que0_prblm.grid(row=1,columnspan=2,sticky='nsew')
que0_solu_label_frame=Frame(que0,bg='#212121') 
Label(que0_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que0_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que0_user_sol=Frame(que0,bg='#212121') 
que0_user_sol.grid_rowconfigure(0,weight=1)
que0_user_sol.grid_rowconfigure(1,weight=1)
que0_user_sol.grid_columnconfigure(0,weight=1) 
que0_user_sol.grid_columnconfigure(1,weight=1) 
que0_user_sol.grid_columnconfigure(2,weight=1) 
que0_user_sol.grid_columnconfigure(3,weight=1) 
que0_user_sol.grid_columnconfigure(4,weight=1) 
que0_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que0_sol1=StringVar()
que0_sol2=StringVar()
que0_sol3=StringVar()
que0_sol1.set("CREATE")
ttk.Entry(que0_user_sol,font=('Arial 12 bold'),textvariable=que0_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que0_user_sol,font=('Arial 12 bold'),textvariable=que0_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que0_user_sol,font=('Arial 12 bold'),textvariable=que0_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que0_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(0)).grid(row=0,column=3,padx=5)
Button(que0_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(0)).pack(side=RIGHT,padx=30)
Button(que0_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(0)).pack(side=RIGHT,padx=60)
que0_full_query=Label(que0,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que0_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que0_success_ack=Label(que0,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que0_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que1=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que1.grid_propagate(False) 
que1.grid_columnconfigure(0,weight=1)
que1.grid_columnconfigure(1,weight=1)
que1.grid_rowconfigure(0,weight=1)
que1.grid_rowconfigure(1,weight=1)
que1.grid_rowconfigure(2,weight=1)
que1.grid_rowconfigure(3,weight=1)
que1.grid_rowconfigure(4,weight=1)
que1.grid_rowconfigure(5,weight=1)
que1.grid_rowconfigure(6,weight=1)
que1.grid_rowconfigure(7,weight=1)
que1_header_frame=Frame(que1,bg='#212121',bd=5,relief='sunken') 
Label(que1_header_frame,text=topics_list_ui1[1],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que1_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(1)).pack(side=RIGHT,padx=30)
que1_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que1_prblm_text='''Q: Delete/Remove a database with name "TUTORINGSYSTEM"'''
que1_prblm=Label(que1,text=que1_prblm_text,font=('Arial 12 bold'),padx=20)
que1_prblm.grid(row=1,columnspan=2,sticky='nsew')
que1_solu_label_frame=Frame(que1,bg='#212121') 
Label(que1_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que1_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que1_user_sol=Frame(que1,bg='#212121') 
que1_user_sol.grid_rowconfigure(0,weight=1)
que1_user_sol.grid_rowconfigure(1,weight=1)
que1_user_sol.grid_columnconfigure(0,weight=1) 
que1_user_sol.grid_columnconfigure(1,weight=1) 
que1_user_sol.grid_columnconfigure(2,weight=1) 
que1_user_sol.grid_columnconfigure(3,weight=1) 
que1_user_sol.grid_columnconfigure(4,weight=1) 
que1_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que1_sol1=StringVar()
que1_sol2=StringVar()
que1_sol3=StringVar()
que1_sol1.set("DROP")
ttk.Entry(que1_user_sol,font=('Arial 12 bold'),textvariable=que1_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que1_user_sol,font=('Arial 12 bold'),textvariable=que1_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que1_user_sol,font=('Arial 12 bold'),textvariable=que1_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que1_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(1)).grid(row=0,column=3,padx=5)
Button(que1_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(1)).pack(side=RIGHT,padx=30)
Button(que1_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(1)).pack(side=RIGHT,padx=60)
que1_full_query=Label(que1,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que1_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que1_success_ack=Label(que1,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que1_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que2=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que2.grid_propagate(False) 
que2.grid_columnconfigure(0,weight=1)
que2.grid_columnconfigure(1,weight=1)
que2.grid_rowconfigure(0,weight=1)
que2.grid_rowconfigure(1,weight=1)
que2.grid_rowconfigure(2,weight=1)
que2.grid_rowconfigure(3,weight=1)
que2.grid_rowconfigure(4,weight=1)
que2.grid_rowconfigure(5,weight=1)
que2.grid_rowconfigure(6,weight=1)
que2.grid_rowconfigure(7,weight=1)
que2_header_frame=Frame(que2,bg='#212121',bd=5,relief='sunken') 
Label(que2_header_frame,text=topics_list_ui1[2],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que2_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(2)).pack(side=RIGHT,padx=30)
que2_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que2_prblm_text='''Q: To list the databases in your machine'''
que2_prblm=Label(que2,text=que2_prblm_text,font=('Arial 12 bold'),padx=20)
que2_prblm.grid(row=1,columnspan=2,sticky='nsew')
que2_solu_label_frame=Frame(que2,bg='#212121') 
Label(que2_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que2_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que2_user_sol=Frame(que2,bg='#212121') 
que2_user_sol.grid_rowconfigure(0,weight=1)
que2_user_sol.grid_rowconfigure(1,weight=1)
que2_user_sol.grid_columnconfigure(0,weight=1) 
que2_user_sol.grid_columnconfigure(1,weight=1) 
que2_user_sol.grid_columnconfigure(2,weight=1) 
que2_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que2_sol1=StringVar()
que2_sol2=StringVar()
que2_sol2.set("DATABASES;")
ttk.Entry(que2_user_sol,font=('Arial 12 bold'),textvariable=que2_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que2_user_sol,font=('Arial 12 bold'),textvariable=que2_sol2,width=20).grid(row=0,column=1,padx=30)
Button(que2_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(2)).grid(row=0,column=2,padx=5)
Button(que2_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(2)).pack(side=RIGHT,padx=30)
Button(que2_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(2)).pack(side=RIGHT,padx=60)
que2_full_query=Label(que2,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que2_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que2_success_ack=Label(que2,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que2_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que3=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que3.grid_propagate(False) 
que3.grid_columnconfigure(0,weight=1)
que3.grid_columnconfigure(1,weight=1)
que3.grid_rowconfigure(0,weight=1)
que3.grid_rowconfigure(1,weight=1)
que3.grid_rowconfigure(2,weight=1)
que3.grid_rowconfigure(3,weight=1)
que3.grid_rowconfigure(4,weight=1)
que3.grid_rowconfigure(5,weight=1)
que3.grid_rowconfigure(6,weight=1)
que3.grid_rowconfigure(7,weight=1)
que3_header_frame=Frame(que3,bg='#212121',bd=5,relief='sunken') 
Label(que3_header_frame,text=topics_list_ui1[3],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que3_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(3)).pack(side=RIGHT,padx=30)
que3_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que3_prblm_text='''Q: Create a table "students" that has 4 columns which are roll, name(atmost 20 characters), year, cgpa respectively'''
que3_prblm=Label(que3,text=que3_prblm_text,font=('Arial 12 bold'),padx=20)
que3_prblm.grid(row=1,columnspan=2,sticky='nsew')
que3_solu_label_frame=Frame(que3,bg='#212121') 
Label(que3_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que3_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que3_user_sol=Frame(que3,bg='#212121') 
que3_user_sol.grid_rowconfigure(0,weight=1)
que3_user_sol.grid_rowconfigure(1,weight=1)
que3_user_sol.grid_columnconfigure(0,weight=1) 
que3_user_sol.grid_columnconfigure(1,weight=1) 
que3_user_sol.grid_columnconfigure(2,weight=1) 
que3_user_sol.grid_columnconfigure(3,weight=1) 
que3_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que3_sol1=StringVar()
que3_sol2=StringVar()
que3_sol3=StringVar()
que3_sol4=StringVar()
que3_sol5=StringVar()
que3_sol6=StringVar()
que3_sol1.set("CREATE TABLE")
que3_sol3.set(" (        INT,")
que3_sol4.set("        VARCHAR(20),")
que3_sol5.set("        INT,")
que3_sol6.set("        FLOAT);")
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol3,width=20).grid(row=0,column=2,padx=30)
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol4,width=20).grid(row=1,column=0,padx=30)
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol5,width=20).grid(row=1,column=1,padx=30)
ttk.Entry(que3_user_sol,font=('Arial 12 bold'),textvariable=que3_sol6,width=20).grid(row=1,column=2,padx=30)
Button(que3_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(3)).grid(row=0,column=3,padx=5)
Button(que3_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(3)).pack(side=RIGHT,padx=30)
Button(que3_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(3)).pack(side=RIGHT,padx=60)
que3_full_query=Label(que3,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que3_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que3_success_ack=Label(que3,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que3_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que4=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que4.grid_propagate(False) 
que4.grid_columnconfigure(0,weight=1)
que4.grid_columnconfigure(1,weight=1)
que4.grid_rowconfigure(0,weight=1)
que4.grid_rowconfigure(1,weight=1)
que4.grid_rowconfigure(2,weight=1)
que4.grid_rowconfigure(3,weight=1)
que4.grid_rowconfigure(4,weight=1)
que4.grid_rowconfigure(5,weight=1)
que4.grid_rowconfigure(6,weight=1)
que4.grid_rowconfigure(7,weight=1)
que4_header_frame=Frame(que4,bg='#212121',bd=5,relief='sunken') 
Label(que4_header_frame,text=topics_list_ui1[4],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que4_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(4)).pack(side=RIGHT,padx=30)
que4_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que4_prblm_text='''Q: Delete/Remove table "students"'''
que4_prblm=Label(que4,text=que4_prblm_text,font=('Arial 12 bold'),padx=20)
que4_prblm.grid(row=1,columnspan=2,sticky='nsew')
que4_solu_label_frame=Frame(que4,bg='#212121') 
Label(que4_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que4_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que4_user_sol=Frame(que4,bg='#212121') 
que4_user_sol.grid_rowconfigure(0,weight=1)
que4_user_sol.grid_rowconfigure(1,weight=1)
que4_user_sol.grid_columnconfigure(0,weight=1) 
que4_user_sol.grid_columnconfigure(1,weight=1) 
que4_user_sol.grid_columnconfigure(2,weight=1) 
que4_user_sol.grid_columnconfigure(3,weight=1) 
que4_user_sol.grid_columnconfigure(4,weight=1) 
que4_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que4_sol1=StringVar()
que4_sol2=StringVar()
que4_sol3=StringVar()
que4_sol1.set("DROP")
ttk.Entry(que4_user_sol,font=('Arial 12 bold'),textvariable=que4_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que4_user_sol,font=('Arial 12 bold'),textvariable=que4_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que4_user_sol,font=('Arial 12 bold'),textvariable=que4_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que4_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(4)).grid(row=0,column=3,padx=5)
Button(que4_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(4)).pack(side=RIGHT,padx=30)
Button(que4_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(4)).pack(side=RIGHT,padx=60)
que4_full_query=Label(que4,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que4_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que4_success_ack=Label(que4,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que4_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que5=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que5.grid_propagate(False) 
que5.grid_columnconfigure(0,weight=1)
que5.grid_columnconfigure(1,weight=1)
que5.grid_rowconfigure(0,weight=1)
que5.grid_rowconfigure(1,weight=1)
que5.grid_rowconfigure(2,weight=1)
que5.grid_rowconfigure(3,weight=1)
que5.grid_rowconfigure(4,weight=1)
que5.grid_rowconfigure(5,weight=1)
que5.grid_rowconfigure(6,weight=1)
que5.grid_rowconfigure(7,weight=1)
que5_header_frame=Frame(que5,bg='#212121',bd=5,relief='sunken') 
Label(que5_header_frame,text=topics_list_ui1[5],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que5_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(5)).pack(side=RIGHT,padx=30)
que5_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que5_prblm_text='''Q: Change the table name of table "students" to "students_itdept" '''
que5_prblm=Label(que5,text=que5_prblm_text,font=('Arial 12 bold'),padx=20)
que5_prblm.grid(row=1,columnspan=2,sticky='nsew')
que5_solu_label_frame=Frame(que5,bg='#212121') 
Label(que5_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que5_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que5_user_sol=Frame(que5,bg='#212121') 
que5_user_sol.grid_rowconfigure(0,weight=1)
que5_user_sol.grid_rowconfigure(1,weight=1)
que5_user_sol.grid_columnconfigure(0,weight=1) 
que5_user_sol.grid_columnconfigure(1,weight=1) 
que5_user_sol.grid_columnconfigure(2,weight=1) 
que5_user_sol.grid_columnconfigure(3,weight=1) 
que5_user_sol.grid_columnconfigure(4,weight=1) 
que5_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que5_sol1=StringVar()
que5_sol2=StringVar()
que5_sol3=StringVar()
que5_sol4=StringVar()
que5_sol1.set("RENAME TABLE")
que5_sol3.set("TO")
ttk.Entry(que5_user_sol,font=('Arial 12 bold'),textvariable=que5_sol1).grid(row=0,column=0,padx=30)
ttk.Entry(que5_user_sol,font=('Arial 12 bold'),textvariable=que5_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que5_user_sol,font=('Arial 12 bold'),textvariable=que5_sol3).grid(row=0,column=2,padx=30)
ttk.Entry(que5_user_sol,font=('Arial 12 bold'),textvariable=que5_sol4,width=20).grid(row=0,column=3,padx=30)
Button(que5_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(5)).grid(row=1,column=3,padx=5)
Button(que5_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(5)).pack(side=RIGHT,padx=30)
Button(que5_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(5)).pack(side=RIGHT,padx=60)
que5_full_query=Label(que5,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que5_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que5_success_ack=Label(que5,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que5_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que6=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que6.grid_propagate(False) 
que6.grid_columnconfigure(0,weight=1)
que6.grid_columnconfigure(1,weight=1)
que6.grid_rowconfigure(0,weight=1)
que6.grid_rowconfigure(1,weight=1)
que6.grid_rowconfigure(2,weight=1)
que6.grid_rowconfigure(3,weight=1)
que6.grid_rowconfigure(4,weight=1)
que6.grid_rowconfigure(5,weight=1)
que6.grid_rowconfigure(6,weight=1)
que6.grid_rowconfigure(7,weight=1)
que6_header_frame=Frame(que6,bg='#212121',bd=5,relief='sunken') 
Label(que6_header_frame,text=topics_list_ui1[6],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que6_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(6)).pack(side=RIGHT,padx=30)
que6_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que6_prblm_text='''Q: Create a table "students" that has 4 columns which are id, name(atmost 20 characters), year, cgpa respectively\nMake column "id" as PRIMARY KEY'''
que6_prblm=Label(que6,text=que6_prblm_text,font=('Arial 12 bold'),padx=20)
que6_prblm.grid(row=1,columnspan=2,sticky='nsew')
que6_solu_label_frame=Frame(que6,bg='#212121') 
Label(que6_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que6_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que6_user_sol=Frame(que6,bg='#212121') 
que6_user_sol.grid_rowconfigure(0,weight=1)
que6_user_sol.grid_rowconfigure(1,weight=1)
que6_user_sol.grid_columnconfigure(0,weight=1) 
que6_user_sol.grid_columnconfigure(1,weight=1) 
que6_user_sol.grid_columnconfigure(2,weight=1) 
que6_user_sol.grid_columnconfigure(3,weight=1) 
que6_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que6_sol1=StringVar()
que6_sol2=StringVar()
que6_sol1.set("CREATE TABLE STUDENTS ( ID INT           ,")
que6_sol2.set("     VARCHAR(20),      INT,      FLOAT);")
ttk.Entry(que6_user_sol,font=('Arial 12 bold'),textvariable=que6_sol1,width=60).grid(row=0,column=0,columnspan=2,padx=30,sticky="w")
ttk.Entry(que6_user_sol,font=('Arial 12 bold'),textvariable=que6_sol2,width=60).grid(row=1,column=0,padx=30,sticky="w")
Button(que6_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(6)).grid(row=0,column=1,padx=30)
Button(que6_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(6)).pack(side=RIGHT,padx=30)
Button(que6_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(6)).pack(side=RIGHT,padx=60)
que6_full_query=Label(que6,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que6_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que6_success_ack=Label(que6,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que6_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")
que6_note_text='''*Note: There are a few ways to do this but please stick to first syntax mentioned in the info provided by "View in Detail"\nSyntax: create table [table_name](  col1_name  col1_datatype  primary key,  col2_name....)'''
que6_note=Label(que6,text=que6_note_text,font=('Arial 10'),padx=20).grid(row=7,columnspan=2,sticky="sew")

que7=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que7.grid_propagate(False) 
que7.grid_columnconfigure(0,weight=1)
que7.grid_columnconfigure(1,weight=1)
que7.grid_rowconfigure(0,weight=1)
que7.grid_rowconfigure(1,weight=1)
que7.grid_rowconfigure(2,weight=1)
que7.grid_rowconfigure(3,weight=1)
que7.grid_rowconfigure(4,weight=1)
que7.grid_rowconfigure(5,weight=1)
que7.grid_rowconfigure(6,weight=1)
que7_header_frame=Frame(que7,bg='#212121',bd=5,relief='sunken') 
Label(que7_header_frame,text=topics_list_ui1[7],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que7_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(7)).pack(side=RIGHT,padx=30)
que7_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que7_prblm_text='''Q: Create a table "student_results" that has 3 columns which are id, name(atmost 20 characters),sgpa respectively,\nGet students(id) column as reference to this table i.e make student_results(id) as foreign key,\nTable:students(id(primary key),name,year,cgpa)  Table:student_results(id(foreign key),name,sgpa)'''
que7_prblm=Label(que7,text=que7_prblm_text,font=('Arial 12 bold'),padx=20)
que7_prblm.grid(row=1,columnspan=2,sticky='nsew')
que7_solu_label_frame=Frame(que7,bg='#212121') 
Label(que7_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que7_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que7_user_sol=Frame(que7,bg='#212121') 
que7_user_sol.grid_rowconfigure(0,weight=1)
que7_user_sol.grid_rowconfigure(1,weight=1)
que7_user_sol.grid_columnconfigure(0,weight=1) 
que7_user_sol.grid_columnconfigure(1,weight=1) 
que7_user_sol.grid_columnconfigure(2,weight=1) 
que7_user_sol.grid_columnconfigure(3,weight=1) 
que7_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que7_sol1=StringVar()
que7_sol2=StringVar()
que7_sol3=StringVar()
que7_sol4=StringVar()
que7_sol1.set("CREATE TABLE STUDENT_RESULTS(ID INT,NAME VARCHAR(20),SGPA FLOAT,")
que7_sol3.set("REFERENCES")
ttk.Entry(que7_user_sol,font=('Arial 12 bold'),textvariable=que7_sol1,width=70).grid(row=0,column=0,columnspan=4,padx=30,sticky="w")
ttk.Entry(que7_user_sol,font=('Arial 12 bold'),textvariable=que7_sol2,width=17).grid(row=1,column=0,padx=30,sticky="w")
ttk.Entry(que7_user_sol,font=('Arial 12 bold'),textvariable=que7_sol3,width=15).grid(row=1,column=1,padx=30,sticky="w")
ttk.Entry(que7_user_sol,font=('Arial 12 bold'),textvariable=que7_sol4,width=15).grid(row=1,column=2,padx=30,sticky="w")
Button(que7_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(7)).grid(row=1,column=3,padx=30)
Button(que7_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(7)).pack(side=RIGHT,padx=30)
Button(que7_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(7)).pack(side=RIGHT,padx=60)
que7_full_query=Label(que7,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que7_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que7_success_ack=Label(que7,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que7_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")
que7_note_text='''*Note: In the syntax you can see "constraint" keyword please do ignore this for now, you can create foreign key without using it.\nSyntax: create table [tablename](col1_name   col1_datatype, col2_name   col2_datatype.....,\nforeign key(column_name) references parent_tablename(column_name)  );'''
que7_note=Label(que7,text=que7_note_text,font=('Arial 10'),padx=20).grid(row=6,columnspan=2,sticky="sew")        


que8=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que8.grid_propagate(False) 
que8.grid_columnconfigure(0,weight=1)
que8.grid_columnconfigure(0,weight=1)
que8.grid_rowconfigure(0,weight=1)
que8.grid_rowconfigure(1,weight=1)
que8.grid_rowconfigure(2,weight=1)
que8.grid_rowconfigure(3,weight=1)
que8.grid_rowconfigure(4,weight=1)
que8.grid_rowconfigure(5,weight=1)
que8.grid_rowconfigure(6,weight=1)
que8.grid_rowconfigure(7,weight=1)
que8_header_frame=Frame(que8,bg="#212121",bd=5,relief="sunken")
Label(que8_header_frame,text=topics_list_ui1[8],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que8_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(8)).pack(side=RIGHT,padx=30)
que8_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que8,text="Alter command is used to change the definition of the table, it can only be used with\nsome other commands like mentioned below, Enter the option to give it a try!",font=('Arial 12 bold'),background='#212121', foreground='White').grid(row=1,columnspan=2,sticky="ew")
Label(que8,text="1.ALTER COMMAND FOR ADDING NEW COLUMN TO TABLE",font=('Arial 12 bold'),padx=20).grid(row=2,columnspan=2,sticky="ew")
Label(que8,text="2.ALTER COMMAND FOR MODIFYING A COLUMN IN THE TABLE",font=('Arial 12 bold'),padx=20).grid(row=3,columnspan=2,sticky="ew")
Label(que8,text="3.ALTER COMMAND FOR DELETING A COLUMN IN THE TABLE",font=('Arial 12 bold'),padx=20).grid(row=4,columnspan=2,sticky="ew")
Label(que8,text="4.ALTER COMMAND FOR RENAMING A COLUMN IN THE TABLE",font=('Arial 12 bold'),padx=20).grid(row=5,columnspan=2,sticky="ew")
Label(que8,text="Enter the option: ",font=('Arial 12 bold'),background='#212121', foreground='White').grid(row=6,column=0,sticky="w",padx=30)
que8_optionentry_value=StringVar()
que8_optionentry=ttk.Entry(que8,font=('Arial 12 bold'),textvariable=que8_optionentry_value,width=5).grid(row=6,column=1,padx=30,sticky="w")
Button(que8,text = "GO",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2", command=alter_subtopic_open).grid(row=7,column=1,padx=30)

que8_1=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que8_1.grid_propagate(False) 
que8_1.grid_columnconfigure(0,weight=1)
que8_1.grid_columnconfigure(0,weight=1)
que8_1.grid_rowconfigure(0,weight=1)
que8_1.grid_rowconfigure(1,weight=1)
que8_1.grid_rowconfigure(2,weight=1)
que8_1.grid_rowconfigure(3,weight=1)
que8_1.grid_rowconfigure(4,weight=1)
que8_1.grid_rowconfigure(5,weight=1)
que8_1.grid_rowconfigure(6,weight=1)
que8_1.grid_rowconfigure(7,weight=1)
que8_1_header_frame=Frame(que8_1,bg="#212121",bd=5,relief="sunken")
Label(que8_1_header_frame,text=topics_list_ui1[8],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que8_1_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(8)).pack(side=RIGHT,padx=30)
que8_1_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que8_1,text="1.ALTER COMMAND FOR ADDING NEW COLUMN TO TABLE\nQ.Add a new column 'PERCENTAGE(FLOAT)' to the table 'RESULTS'\nTable: results(id int,name varchar(20),cgpa float)",font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky="new")
que8_1_user_sol=Frame(que8_1,bg='#212121') 
que8_1_user_sol.grid_rowconfigure(0,weight=1)
que8_1_user_sol.grid_rowconfigure(1,weight=1)
que8_1_user_sol.grid_columnconfigure(0,weight=1) 
que8_1_user_sol.grid_columnconfigure(1,weight=1) 
que8_1_user_sol.grid_columnconfigure(2,weight=1) 
que8_1_user_sol.grid_columnconfigure(3,weight=1) 
que8_1_user_sol.grid_columnconfigure(4,weight=1) 
que8_1_user_sol.grid(row=2,columnspan=2,sticky="nsw")
que8_1_sol1=StringVar()
que8_1_sol2=StringVar()
que8_1_sol3=StringVar()
que8_1_sol1.set("       TABLE RESULTS")
que8_1_sol3.set("PERCENTAGE FLOAT;")
ttk.Entry(que8_1_user_sol,font=('Arial 12 bold'),textvariable=que8_1_sol1,width=25).grid(row=0,column=0,padx=30)
ttk.Entry(que8_1_user_sol,font=('Arial 12 bold'),textvariable=que8_1_sol2,width=15).grid(row=0,column=1,padx=30)
ttk.Entry(que8_1_user_sol,font=('Arial 12 bold'),textvariable=que8_1_sol3,width=21).grid(row=0,column=2,padx=30)
Button(que8_1_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(8.1)).grid(row=1,column=0,padx=30,sticky="w")
Button(que8_1_user_sol,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(8.1)).grid(row=0,column=3)
#Button(que8_1_user_sol,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(8.1)).pack(side=RIGHT,padx=60)
que8_1_full_query=Label(que8_1,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que8_1_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que8_1_success_ack=Label(que8_1,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que8_1_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que8_2=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que8_2.grid_propagate(False) 
que8_2.grid_columnconfigure(0,weight=1)
que8_2.grid_columnconfigure(0,weight=1)
que8_2.grid_rowconfigure(0,weight=1)
que8_2.grid_rowconfigure(1,weight=1)
que8_2.grid_rowconfigure(2,weight=1)
que8_2.grid_rowconfigure(3,weight=1)
que8_2.grid_rowconfigure(4,weight=1)
que8_2.grid_rowconfigure(5,weight=1)
que8_2.grid_rowconfigure(6,weight=1)
que8_2.grid_rowconfigure(7,weight=1)
que8_2_header_frame=Frame(que8_2,bg="#212121",bd=5,relief="sunken")
Label(que8_2_header_frame,text=topics_list_ui1[8],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que8_2_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(8)).pack(side=RIGHT,padx=30)
que8_2_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que8_2,text="2.ALTER COMMAND FOR MODIFYING A COLUMN IN THE TABLE\nQ.Change column name varchar(20) in table 'STUDENTS' to name varchar(40)",font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky="new")
que8_2_user_sol=Frame(que8_2,bg='#212121') 
que8_2_user_sol.grid_rowconfigure(0,weight=1)
que8_2_user_sol.grid_rowconfigure(1,weight=1)
que8_2_user_sol.grid_columnconfigure(0,weight=1) 
que8_2_user_sol.grid_columnconfigure(1,weight=1) 
que8_2_user_sol.grid_columnconfigure(2,weight=1) 
que8_2_user_sol.grid_columnconfigure(3,weight=1) 
que8_2_user_sol.grid_columnconfigure(4,weight=1) 
que8_2_user_sol.grid(row=2,columnspan=2,sticky="nsw")
que8_2_sol1=StringVar()
que8_2_sol2=StringVar()
que8_2_sol3=StringVar()
que8_2_sol1.set("       TABLE STUDENTS")
que8_2_sol3.set("NAME VARCHAR(40);")
ttk.Entry(que8_2_user_sol,font=('Arial 12 bold'),textvariable=que8_2_sol1,width=25).grid(row=0,column=0,padx=30)
ttk.Entry(que8_2_user_sol,font=('Arial 12 bold'),textvariable=que8_2_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que8_2_user_sol,font=('Arial 12 bold'),textvariable=que8_2_sol3,width=25).grid(row=0,column=2,padx=30)
Button(que8_2_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(8.2)).grid(row=0,column=3,padx=30)
Button(que8_2_user_sol,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(8.2)).grid(row=1,column=0,padx=30,sticky="w")
#Button(que8_2_user_sol,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(8.2)).pack(side=RIGHT,padx=60)
que8_2_full_query=Label(que8_2,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que8_2_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que8_2_success_ack=Label(que8_2,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que8_2_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que8_3=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que8_3.grid_propagate(False) 
que8_3.grid_columnconfigure(0,weight=1)
que8_3.grid_columnconfigure(0,weight=1)
que8_3.grid_rowconfigure(0,weight=1)
que8_3.grid_rowconfigure(1,weight=1)
que8_3.grid_rowconfigure(2,weight=1)
que8_3.grid_rowconfigure(3,weight=1)
que8_3.grid_rowconfigure(4,weight=1)
que8_3.grid_rowconfigure(5,weight=1)
que8_3.grid_rowconfigure(6,weight=1)
que8_3.grid_rowconfigure(7,weight=1)
que8_3_header_frame=Frame(que8_3,bg="#212121",bd=5,relief="sunken")
Label(que8_3_header_frame,text=topics_list_ui1[8],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que8_3_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(8)).pack(side=RIGHT,padx=30)
que8_3_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que8_3,text="3.ALTER COMMAND FOR DELETING A COLUMN IN THE TABLE\nQ.Delete column 'CONTACT' in table 'STUDENTS'",font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky="new")
que8_3_user_sol=Frame(que8_3,bg='#212121') 
que8_3_user_sol.grid_rowconfigure(0,weight=1)
que8_3_user_sol.grid_rowconfigure(1,weight=1)
que8_3_user_sol.grid_columnconfigure(0,weight=1) 
que8_3_user_sol.grid_columnconfigure(1,weight=1) 
que8_3_user_sol.grid_columnconfigure(2,weight=1) 
que8_3_user_sol.grid_columnconfigure(3,weight=1) 
que8_3_user_sol.grid_columnconfigure(4,weight=1) 
que8_3_user_sol.grid(row=2,columnspan=2,sticky="nsw")
que8_3_sol1=StringVar()
que8_3_sol2=StringVar()
que8_3_sol3=StringVar()
que8_3_sol1.set("       TABLE STUDENTS")
que8_3_sol3.set("CONTACT;")
ttk.Entry(que8_3_user_sol,font=('Arial 12 bold'),textvariable=que8_3_sol1,width=25).grid(row=0,column=0,padx=30)
ttk.Entry(que8_3_user_sol,font=('Arial 12 bold'),textvariable=que8_3_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que8_3_user_sol,font=('Arial 12 bold'),textvariable=que8_3_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que8_3_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(8.3)).grid(row=0,column=3,padx=30)
Button(que8_3_user_sol,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(8.3)).grid(row=1,column=0,padx=30,sticky="w")
#Button(que8_3_user_sol,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(8.3)).pack(side=RIGHT,padx=60)
que8_3_full_query=Label(que8_3,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que8_3_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que8_3_success_ack=Label(que8_3,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que8_3_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que8_4=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que8_4.grid_propagate(False) 
que8_4.grid_columnconfigure(0,weight=1)
que8_4.grid_columnconfigure(0,weight=1)
que8_4.grid_rowconfigure(0,weight=1)
que8_4.grid_rowconfigure(1,weight=1)
que8_4.grid_rowconfigure(2,weight=1)
que8_4.grid_rowconfigure(3,weight=1)
que8_4.grid_rowconfigure(4,weight=1)
que8_4.grid_rowconfigure(5,weight=1)
que8_4.grid_rowconfigure(6,weight=1)
que8_4.grid_rowconfigure(7,weight=1)
que8_4_header_frame=Frame(que8_4,bg="#212121",bd=5,relief="sunken")
Label(que8_4_header_frame,text=topics_list_ui1[8],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que8_4_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(8)).pack(side=RIGHT,padx=30)
que8_4_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que8_4,text="4.ALTER COMMAND FOR RENAMING A COLUMN IN THE TABLE\nQ.Rename column 'id' to'student_id' in table 'STUDENTS'",font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky="new")
que8_4_user_sol=Frame(que8_4,bg='#212121') 
que8_4_user_sol.grid_rowconfigure(0,weight=1)
que8_4_user_sol.grid_rowconfigure(1,weight=1)
que8_4_user_sol.grid_columnconfigure(0,weight=1) 
que8_4_user_sol.grid_columnconfigure(1,weight=1) 
que8_4_user_sol.grid_columnconfigure(2,weight=1) 
que8_4_user_sol.grid_columnconfigure(3,weight=1) 
que8_4_user_sol.grid_columnconfigure(4,weight=1) 
que8_4_user_sol.grid(row=2,columnspan=2,sticky="nsw")
que8_4_sol1=StringVar()
que8_4_sol2=StringVar()
que8_4_sol3=StringVar()
que8_4_sol1.set("       TABLE STUDENTS")
que8_4_sol3.set("ID STUDENT_ID INT;")
ttk.Entry(que8_4_user_sol,font=('Arial 12 bold'),textvariable=que8_4_sol1,width=23).grid(row=0,column=0,padx=30)
ttk.Entry(que8_4_user_sol,font=('Arial 12 bold'),textvariable=que8_4_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que8_4_user_sol,font=('Arial 12 bold'),textvariable=que8_4_sol3,width=23).grid(row=0,column=2,padx=30)
Button(que8_4_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(8.4)).grid(row=0,column=3,padx=30)
Button(que8_4_user_sol,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(8.4)).grid(row=1,column=0,padx=30,sticky="w")
#Button(que8_4_user_sol,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(8.4)).pack(side=RIGHT,padx=60)
que8_4_full_query=Label(que8_4,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que8_4_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que8_4_success_ack=Label(que8_4,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que8_4_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que9=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que9.grid_propagate(False) 
que9.grid_columnconfigure(0,weight=1)
que9.grid_columnconfigure(1,weight=1)
que9.grid_rowconfigure(0,weight=1)
que9.grid_rowconfigure(1,weight=1)
que9.grid_rowconfigure(2,weight=1)
que9.grid_rowconfigure(3,weight=1)
que9.grid_rowconfigure(4,weight=1)
que9.grid_rowconfigure(5,weight=1)
que9.grid_rowconfigure(6,weight=1)
que9.grid_rowconfigure(7,weight=1)
que9_header_frame=Frame(que9,bg='#212121',bd=5,relief='sunken') 
Label(que9_header_frame,text=topics_list_ui1[9],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que9_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(9)).pack(side=RIGHT,padx=30)
que9_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que9_prblm_text='''Q: Insert data:-  (3000,"Ironman",1) into table Avengers(id,Name,Ranked)'''
que9_prblm=Label(que9,text=que9_prblm_text,font=('Arial 12 bold'),padx=20)
que9_prblm.grid(row=1,columnspan=2,sticky='nsew')
que9_solu_label_frame=Frame(que9,bg='#212121') 
Label(que9_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que9_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que9_user_sol=Frame(que9,bg='#212121') 
que9_user_sol.grid_rowconfigure(0,weight=1)
que9_user_sol.grid_rowconfigure(1,weight=1)
que9_user_sol.grid_columnconfigure(0,weight=1) 
que9_user_sol.grid_columnconfigure(1,weight=1) 
que9_user_sol.grid_columnconfigure(2,weight=1) 
que9_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que9_sol1=StringVar()
que9_sol2=StringVar()
que9_sol3=StringVar()
que9_sol1.set("INSERT INTO")
que9_sol3.set("VALUES(                 ,                  ,                );")
ttk.Entry(que9_user_sol,font=('Arial 12 bold'),textvariable=que9_sol1,width=20).grid(row=0,column=0,padx=30,sticky="w")
ttk.Entry(que9_user_sol,font=('Arial 12 bold'),textvariable=que9_sol2,width=20).grid(row=0,column=1,sticky="w")
Button(que9_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(9)).grid(row=0,column=2,padx=30)
ttk.Entry(que9_user_sol,font=('Arial 12 bold'),textvariable=que9_sol3,width=60).grid(row=1,columnspan=2,padx=30)
Button(que9_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(9)).pack(side=RIGHT,padx=30)
Button(que9_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(9)).pack(side=RIGHT,padx=60)
que9_full_query=Label(que9,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que9_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que9_success_ack=Label(que9,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que9_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")
que9_note_text='''*Note: if you see the info in "View in detail" you can see various ways of insertion into a table\nWhile we only concentrate on one way you need to learn all the ways of insertion'''
que9_note=Label(que9,text=que9_note_text,font=('Arial 10'),padx=20).grid(row=7,columnspan=2,sticky="sew")


que10=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que10.grid_propagate(False) 
que10.grid_columnconfigure(0,weight=1)
que10.grid_columnconfigure(1,weight=1)
que10.grid_rowconfigure(0,weight=1)
que10.grid_rowconfigure(1,weight=1)
que10.grid_rowconfigure(2,weight=1)
que10.grid_rowconfigure(3,weight=1)
que10.grid_rowconfigure(4,weight=1)
que10.grid_rowconfigure(5,weight=1)
que10.grid_rowconfigure(6,weight=1)
que10.grid_rowconfigure(7,weight=1)
que10_header_frame=Frame(que10,bg='#212121',bd=5,relief='sunken') 
Label(que10_header_frame,text=topics_list_ui1[10],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que10_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(10)).pack(side=RIGHT,padx=30)
que10_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que10_prblm_text='''Q: Delete data in table "Avengers(id,Name,Ranked)" whose rank is 1'''
que10_prblm=Label(que10,text=que10_prblm_text,font=('Arial 12 bold'),padx=20)
que10_prblm.grid(row=1,columnspan=2,sticky='nsew')
que10_solu_label_frame=Frame(que10,bg='#212121') 
Label(que10_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que10_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que10_user_sol=Frame(que10,bg='#212121') 
que10_user_sol.grid_rowconfigure(0,weight=1)
que10_user_sol.grid_rowconfigure(1,weight=1)
que10_user_sol.grid_columnconfigure(0,weight=1) 
que10_user_sol.grid_columnconfigure(1,weight=1) 
que10_user_sol.grid_columnconfigure(2,weight=1) 
que10_user_sol.grid_columnconfigure(3,weight=1) 
que10_user_sol.grid_columnconfigure(4,weight=1) 
que10_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que10_sol1=StringVar()
que10_sol2=StringVar()
que10_sol3=StringVar()
que10_sol4=StringVar()
que10_sol1.set("DELETE FROM")
que10_sol3.set("WHERE")
ttk.Entry(que10_user_sol,font=('Arial 12 bold'),textvariable=que10_sol1).grid(row=0,column=0,padx=30)
ttk.Entry(que10_user_sol,font=('Arial 12 bold'),textvariable=que10_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que10_user_sol,font=('Arial 12 bold'),textvariable=que10_sol3).grid(row=0,column=2,padx=30)
ttk.Entry(que10_user_sol,font=('Arial 12 bold'),textvariable=que10_sol4,width=20).grid(row=0,column=3,padx=30)
Button(que10_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(10)).grid(row=1,column=3,padx=5)
Button(que10_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(10)).pack(side=RIGHT,padx=30)
Button(que10_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(10)).pack(side=RIGHT,padx=60)
que10_full_query=Label(que10,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que10_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que10_success_ack=Label(que10,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que10_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que11=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que11.grid_propagate(False) 
que11.grid_columnconfigure(0,weight=1)
que11.grid_columnconfigure(1,weight=1)
que11.grid_rowconfigure(0,weight=1)
que11.grid_rowconfigure(1,weight=1)
que11.grid_rowconfigure(2,weight=1)
que11.grid_rowconfigure(3,weight=1)
que11.grid_rowconfigure(4,weight=1)
que11.grid_rowconfigure(5,weight=1)
que11.grid_rowconfigure(6,weight=1)
que11.grid_rowconfigure(7,weight=1)
que11_header_frame=Frame(que11,bg='#212121',bd=5,relief='sunken') 
Label(que11_header_frame,text=topics_list_ui1[11],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que11_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(11)).pack(side=RIGHT,padx=30)
que11_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que11_prblm_text='''Q: Update data in table "Avengers(id,Name,Ranked)" change id to 1 whose id is 3000 '''
que11_prblm=Label(que11,text=que11_prblm_text,font=('Arial 12 bold'),padx=20)
que11_prblm.grid(row=1,columnspan=2,sticky='nsew')
que11_solu_label_frame=Frame(que11,bg='#212121') 
Label(que11_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que11_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que11_user_sol=Frame(que11,bg='#212121') 
que11_user_sol.grid_rowconfigure(0,weight=1)
que11_user_sol.grid_rowconfigure(1,weight=1)
que11_user_sol.grid_columnconfigure(0,weight=1) 
que11_user_sol.grid_columnconfigure(1,weight=1) 
que11_user_sol.grid_columnconfigure(2,weight=1) 
que11_user_sol.grid_columnconfigure(3,weight=1) 
que11_user_sol.grid_columnconfigure(4,weight=1) 
que11_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que11_sol1=StringVar()
que11_sol2=StringVar()
que11_sol3=StringVar()
que11_sol1.set("UPDATE AVENGERS")
que11_sol2.set("SET")
que11_sol3.set("WHERE")
ttk.Entry(que11_user_sol,font=('Arial 12 bold'),textvariable=que11_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que11_user_sol,font=('Arial 12 bold'),textvariable=que11_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que11_user_sol,font=('Arial 12 bold'),textvariable=que11_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que11_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(11)).grid(row=0,column=3,padx=5)
Button(que11_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(11)).pack(side=RIGHT,padx=30)
Button(que11_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(11)).pack(side=RIGHT,padx=60)
que11_full_query=Label(que11,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que11_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que11_success_ack=Label(que11,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que11_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que12=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que12.grid_propagate(False) 
que12.grid_columnconfigure(0,weight=1)
que12.grid_columnconfigure(0,weight=1)
que12.grid_rowconfigure(0,weight=1)
que12.grid_rowconfigure(1,weight=1)
que12.grid_rowconfigure(2,weight=1)
que12.grid_rowconfigure(3,weight=1)
que12.grid_rowconfigure(4,weight=1)
que12.grid_rowconfigure(5,weight=1)
que12.grid_rowconfigure(6,weight=1)
que12.grid_rowconfigure(7,weight=1)
que12_header_frame=Frame(que12,bg="#212121",bd=5,relief="sunken")
Label(que12_header_frame,text=topics_list_ui1[12],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que12_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(12)).pack(side=RIGHT,padx=30)
que12_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que12,text="1. If we want to retrieve a single column from the table, we need to execute the below query:",font=('Arial 12'),padx=10,background='#212121', foreground='White',justify='left').grid(row=1,sticky="w")
Label(que12,text="mysql> SELECT Name FROM employee_detail;",font=('Arial 13 bold'),padx=20).grid(row=2,columnspan=2,sticky="ew",padx=10)
Label(que12,text="2. If we want to query multiple columns from the table, we need to execute the below query:",font=('Arial 12'),padx=10,background='#212121', foreground='White',justify='left').grid(row=3,sticky="w")
Label(que12,text="mysql> SELECT Name, Email, City FROM employee_detail;",font=('Arial 13 bold'),padx=20).grid(row=4,columnspan=2,sticky="ew",padx=10)
Label(que12,text="3. If we want to fetch data from all columns of the table, MySQL uses an asterisk (*) to retrieve all column data as follows:",font=('Arial 12'),padx=10,background='#212121', foreground='White',justify='left').grid(row=5,sticky="w")
Label(que12,text="mysql> SELECT * FROM employee_detail;",font=('Arial 13 bold'),padx=20).grid(row=6,columnspan=2,sticky="ew",padx=10)
Label(que12,text="4. Here, we use the SUM function with the HAVING clause in the SELECT command to get the employee name, city, and total\nworking hours.Also, it uses the GROUP BY clause to group them by the Name column.",font=('Arial 12'),padx=10,background='#212121', foreground='White',justify='left').grid(row=7,sticky="w")
Label(que12,text="SELECT Name, City, SUM(working_hours) AS 'Total working hours'\nFROM employee_detail\nGROUP BY Name\nHAVING SUM(working_hours) > 5;",font=('Arial 13 bold'),padx=20).grid(row=8,columnspan=2,sticky="ew",padx=10)

que13=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que13.grid_propagate(False) 
que13.grid_columnconfigure(0,weight=1)
que13.grid_columnconfigure(1,weight=1)
que13.grid_rowconfigure(0,weight=1)
que13.grid_rowconfigure(1,weight=1)
que13.grid_rowconfigure(2,weight=1)
que13.grid_rowconfigure(3,weight=1)
que13.grid_rowconfigure(4,weight=1)
que13.grid_rowconfigure(5,weight=1)
que13.grid_rowconfigure(6,weight=1)
que13.grid_rowconfigure(7,weight=1)
que13_header_frame=Frame(que13,bg='#212121',bd=5,relief='sunken') 
Label(que13_header_frame,text=topics_list_ui1[13],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que13_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(13)).pack(side=RIGHT,padx=30)
que13_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que13_prblm_text='''Q: To list ALL TABLES in the databse "ITS"'''
que13_prblm=Label(que13,text=que13_prblm_text,font=('Arial 12 bold'),padx=20)
que13_prblm.grid(row=1,columnspan=2,sticky='nsew')
que13_solu_label_frame=Frame(que13,bg='#212121') 
Label(que13_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que13_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que13_user_sol=Frame(que13,bg='#212121') 
que13_user_sol.grid_rowconfigure(0,weight=1)
que13_user_sol.grid_rowconfigure(1,weight=1)
que13_user_sol.grid_columnconfigure(0,weight=1) 
que13_user_sol.grid_columnconfigure(1,weight=1) 
que13_user_sol.grid_columnconfigure(2,weight=1) 
que13_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que13_sol1=StringVar()
que13_sol2=StringVar()
que13_sol2.set("TABLES;")
ttk.Entry(que13_user_sol,font=('Arial 12 bold'),textvariable=que13_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que13_user_sol,font=('Arial 12 bold'),textvariable=que13_sol2,width=20).grid(row=0,column=1,padx=30)
Button(que13_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(13)).grid(row=0,column=2,padx=5)
Button(que13_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(13)).pack(side=RIGHT,padx=30)
Button(que13_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(13)).pack(side=RIGHT,padx=60)
que13_full_query=Label(que13,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que13_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que13_success_ack=Label(que13,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que13_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que14=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que14.grid_propagate(False)
que14.grid_columnconfigure(0,weight=1)
que14.grid_columnconfigure(0,weight=1)
que14.grid_rowconfigure(0,weight=1)
que14.grid_rowconfigure(1,weight=1)
que14.grid_rowconfigure(2,weight=1)
que14.grid_rowconfigure(3,weight=1)
que14.grid_rowconfigure(4,weight=1)
que14.grid_rowconfigure(5,weight=1)
que14.grid_rowconfigure(6,weight=1)
que14.grid_rowconfigure(7,weight=1)
que14_header_frame=Frame(que14,bg="#212121",bd=5,relief="sunken")
Label(que14_header_frame,text=topics_list_ui1[14],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que14_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(14)).pack(side=RIGHT,padx=30)
que14_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que14_prblm_text='''Q: Print the details of the person in the table 'EMPLOYEES' whose EmpId is 120\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))\nData in the Table:\n(155,'Srikanth',42000,'ItSolution')\n(120,'Ashwin',50000,'HrOperations')'''
que14_prblm=Label(que14,text=que14_prblm_text,font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky='new')
que14_solu_label_frame=Frame(que14,bg='#212121') 
Label(que14_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que14_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que14_user_sol=Frame(que14,bg='#212121') 
que14_user_sol.grid_rowconfigure(0,weight=1)
que14_user_sol.grid_rowconfigure(1,weight=1)
que14_user_sol.grid_columnconfigure(0,weight=1) 
que14_user_sol.grid_columnconfigure(1,weight=1) 
que14_user_sol.grid_columnconfigure(2,weight=1) 
que14_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que14_sol1=StringVar()
que14_sol2=StringVar()
que14_sol3=StringVar()
que14_sol1.set("SELECT * FROM EMPLOYEES")
que14_sol3.set("EMPID=")
ttk.Entry(que14_user_sol,font=('Arial 12 bold'),textvariable=que14_sol1,width=30).grid(row=0,column=0,padx=30,sticky="w")
ttk.Entry(que14_user_sol,font=('Arial 12 bold'),textvariable=que14_sol2,width=18).grid(row=0,column=1,padx=30,sticky="w")
ttk.Entry(que14_user_sol,font=('Arial 12 bold'),textvariable=que14_sol3,width=18).grid(row=0,column=2,padx=30,sticky="w")
Button(que14_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(14)).grid(row=0,column=3,padx=5)
Button(que14_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(14)).pack(side=RIGHT,padx=30)
Button(que14_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(14)).pack(side=RIGHT,padx=60)
que14_full_query=Label(que14,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que14_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que14_success_ack=Label(que14,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que14_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")


que15=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que15.grid_propagate(False)
que15.grid_columnconfigure(0,weight=1)
que15.grid_columnconfigure(0,weight=1)
que15.grid_rowconfigure(0,weight=1)
que15.grid_rowconfigure(1,weight=1)
que15.grid_rowconfigure(2,weight=1)
que15.grid_rowconfigure(3,weight=1)
que15.grid_rowconfigure(4,weight=1)
que15.grid_rowconfigure(5,weight=1)
que15.grid_rowconfigure(6,weight=1)
que15.grid_rowconfigure(7,weight=1)
que15_header_frame=Frame(que15,bg="#212121",bd=5,relief="sunken")
Label(que15_header_frame,text=topics_list_ui1[15],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que15_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(15)).pack(side=RIGHT,padx=30)
que15_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que15_prblm_text='''Q: Apply distinct clause on the column Salary in table\nEmployees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que15_prblm=Label(que15,text=que15_prblm_text,font=('Arial 12 bold'),padx=20).grid(row=1,columnspan=2,sticky='nsew')
que15_solu_label_frame=Frame(que15,bg='#212121') 
Label(que15_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que15_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que15_user_sol=Frame(que15,bg='#212121') 
que15_user_sol.grid_rowconfigure(0,weight=1)
que15_user_sol.grid_rowconfigure(1,weight=1)
que15_user_sol.grid_columnconfigure(0,weight=1) 
que15_user_sol.grid_columnconfigure(1,weight=1) 
que15_user_sol.grid_columnconfigure(2,weight=1) 
que15_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que15_sol1=StringVar()
que15_sol2=StringVar()
que15_sol3=StringVar()
que15_sol1.set("SELECT")
que15_sol2.set("SALARY")
que15_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que15_user_sol,font=('Arial 12 bold'),textvariable=que15_sol1,width=20).grid(row=0,column=0,padx=30,sticky="w")
ttk.Entry(que15_user_sol,font=('Arial 12 bold'),textvariable=que15_sol2,width=18).grid(row=0,column=1,padx=30,sticky="w")
ttk.Entry(que15_user_sol,font=('Arial 12 bold'),textvariable=que15_sol3,width=20).grid(row=0,column=2,padx=30,sticky="w")
Button(que15_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(15)).grid(row=0,column=3,padx=5)
Button(que15_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(15)).pack(side=RIGHT,padx=30)
Button(que15_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(15)).pack(side=RIGHT,padx=60)
que15_full_query=Label(que15,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que15_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que15_success_ack=Label(que15,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que15_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que16=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que16.grid_propagate(False) 
que16.grid_columnconfigure(0,weight=1)
que16.grid_columnconfigure(1,weight=1)
que16.grid_rowconfigure(0,weight=1)
que16.grid_rowconfigure(1,weight=1)
que16.grid_rowconfigure(2,weight=1)
que16.grid_rowconfigure(3,weight=1)
que16.grid_rowconfigure(4,weight=1)
que16.grid_rowconfigure(5,weight=1)
que16.grid_rowconfigure(6,weight=1)
que16.grid_rowconfigure(7,weight=1)
que16_header_frame=Frame(que16,bg='#212121',bd=5,relief='sunken') 
Label(que16_header_frame,text=topics_list_ui1[16],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que16_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(6)).pack(side=RIGHT,padx=30)
que16_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que16_prblm_text='''Q: Sort the data in the table Employees according to their salries\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que16_prblm=Label(que16,text=que16_prblm_text,font=('Arial 12 bold'),padx=20)
que16_prblm.grid(row=1,columnspan=2,sticky='nsew')
que16_solu_label_frame=Frame(que16,bg='#212121') 
Label(que16_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que16_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que16_user_sol=Frame(que16,bg='#212121') 
que16_user_sol.grid_rowconfigure(0,weight=1)
que16_user_sol.grid_rowconfigure(1,weight=1)
que16_user_sol.grid_columnconfigure(0,weight=1) 
que16_user_sol.grid_columnconfigure(1,weight=1) 
que16_user_sol.grid_columnconfigure(2,weight=1) 
que16_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que16_sol1=StringVar()
que16_sol2=StringVar()
que16_sol2.set("ORDER BY    ;")
ttk.Entry(que16_user_sol,font=('Arial 12 bold'),textvariable=que16_sol1,width=30).grid(row=0,column=0,padx=30)
ttk.Entry(que16_user_sol,font=('Arial 12 bold'),textvariable=que16_sol2,width=20).grid(row=0,column=1,padx=30)
Button(que16_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(16)).grid(row=0,column=2,padx=5)
Button(que16_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(16)).pack(side=RIGHT,padx=30)
Button(que16_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(16)).pack(side=RIGHT,padx=60)
que16_full_query=Label(que16,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que16_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que16_success_ack=Label(que16,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que16_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que17=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que17.grid_propagate(False) 
que17.grid_columnconfigure(0,weight=1)
que17.grid_columnconfigure(1,weight=1)
que17.grid_rowconfigure(0,weight=1)
que17.grid_rowconfigure(1,weight=1)
que17.grid_rowconfigure(2,weight=1)
que17.grid_rowconfigure(3,weight=1)
que17.grid_rowconfigure(4,weight=1)
que17.grid_rowconfigure(5,weight=1)
que17.grid_rowconfigure(6,weight=1)
que17.grid_rowconfigure(7,weight=1)
que17_header_frame=Frame(que17,bg='#212121',bd=5,relief='sunken') 
Label(que17_header_frame,text=topics_list_ui1[17],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que17_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(6)).pack(side=RIGHT,padx=30)
que17_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que17_prblm_text='''Q: Group the data in the table Employees according to their department\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que17_prblm=Label(que17,text=que17_prblm_text,font=('Arial 12 bold'),padx=20)
que17_prblm.grid(row=1,columnspan=2,sticky='nsew')
que17_solu_label_frame=Frame(que17,bg='#212121') 
Label(que17_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que17_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que17_user_sol=Frame(que17,bg='#212121') 
que17_user_sol.grid_rowconfigure(0,weight=1)
que17_user_sol.grid_rowconfigure(1,weight=1)
que17_user_sol.grid_columnconfigure(0,weight=1) 
que17_user_sol.grid_columnconfigure(1,weight=1) 
que17_user_sol.grid_columnconfigure(2,weight=1) 
que17_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que17_sol1=StringVar()
que17_sol2=StringVar()
que17_sol2.set("GROUP BY    ;")
ttk.Entry(que17_user_sol,font=('Arial 12 bold'),textvariable=que17_sol1,width=30).grid(row=0,column=0,padx=30)
ttk.Entry(que17_user_sol,font=('Arial 12 bold'),textvariable=que17_sol2,width=25).grid(row=0,column=1,padx=30)
Button(que17_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(17)).grid(row=0,column=2,padx=5)
Button(que17_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(17)).pack(side=RIGHT,padx=30)
Button(que17_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(17)).pack(side=RIGHT,padx=60)
que17_full_query=Label(que17,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que17_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que17_success_ack=Label(que17,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que17_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que18=Frame(ui_frame_level1,bd=5,bg="#212121",relief="sunken")
que18.grid_propagate(False)  
que18.grid_columnconfigure(0,weight=1)
que18.grid_columnconfigure(0,weight=1)
que18.grid_rowconfigure(0,weight=1)
que18.grid_rowconfigure(1,weight=1)
que18_header_frame=Frame(que18,bg="#212121",bd=5,relief="sunken")
Label(que18_header_frame,text=topics_list_ui1[18],font=("Arial 14 bold"),padx=20).pack(side=LEFT,padx=30)
Button(que18_header_frame,text = "View in Detail",bg="#5b83ba",font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(18)).pack(side=RIGHT,padx=30)
que18_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
Label(que18,text="MySQL 'HAVING' Clause is used with GROUP BY clause. It always returns the rows where condition is TRUE.\n\nYou can get the related information in 'View in Detail' Button",font=('Arial 12 bold')).grid(row=1,columnspan=2,sticky="nsew")

que19=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que19.grid_propagate(False) 
que19.grid_columnconfigure(0,weight=1)
que19.grid_columnconfigure(1,weight=1)
que19.grid_rowconfigure(0,weight=1)
que19.grid_rowconfigure(1,weight=1)
que19.grid_rowconfigure(2,weight=1)
que19.grid_rowconfigure(3,weight=1)
que19.grid_rowconfigure(4,weight=1)
que19.grid_rowconfigure(5,weight=1)
que19.grid_rowconfigure(6,weight=1)
que19.grid_rowconfigure(7,weight=1)
que19_header_frame=Frame(que19,bg='#212121',bd=5,relief='sunken') 
Label(que19_header_frame,text=topics_list_ui1[19],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que19_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(19)).pack(side=RIGHT,padx=30)
que19_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que19_prblm_text='''Q: Print total Number of rows in the table "Employees"'''
que19_prblm=Label(que19,text=que19_prblm_text,font=('Arial 12 bold'),padx=20)
que19_prblm.grid(row=1,columnspan=2,sticky='nsew')
que19_solu_label_frame=Frame(que19,bg='#212121') 
Label(que19_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que19_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que19_user_sol=Frame(que19,bg='#212121') 
que19_user_sol.grid_rowconfigure(0,weight=1)
que19_user_sol.grid_rowconfigure(1,weight=1)
que19_user_sol.grid_columnconfigure(0,weight=1) 
que19_user_sol.grid_columnconfigure(1,weight=1) 
que19_user_sol.grid_columnconfigure(2,weight=1) 
que19_user_sol.grid_columnconfigure(3,weight=1) 
que19_user_sol.grid_columnconfigure(4,weight=1) 
que19_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que19_sol1=StringVar()
que19_sol2=StringVar()
que19_sol3=StringVar()
que19_sol1.set("SELECT")
que19_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que19_user_sol,font=('Arial 12 bold'),textvariable=que19_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que19_user_sol,font=('Arial 12 bold'),textvariable=que19_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que19_user_sol,font=('Arial 12 bold'),textvariable=que19_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que19_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(19)).grid(row=0,column=3,padx=5)
Button(que19_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(19)).pack(side=RIGHT,padx=30)
Button(que19_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(19)).pack(side=RIGHT,padx=60)
que19_full_query=Label(que19,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que19_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que19_success_ack=Label(que19,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que19_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que20=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que20.grid_propagate(False) 
que20.grid_columnconfigure(0,weight=1)
que20.grid_columnconfigure(1,weight=1)
que20.grid_rowconfigure(0,weight=1)
que20.grid_rowconfigure(1,weight=1)
que20.grid_rowconfigure(2,weight=1)
que20.grid_rowconfigure(3,weight=1)
que20.grid_rowconfigure(4,weight=1)
que20.grid_rowconfigure(5,weight=1)
que20.grid_rowconfigure(6,weight=1)
que20.grid_rowconfigure(7,weight=1)
que20_header_frame=Frame(que20,bg='#212121',bd=5,relief='sunken') 
Label(que20_header_frame,text=topics_list_ui1[20],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que20_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(20)).pack(side=RIGHT,padx=30)
que20_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que20_prblm_text='''Q: Print the SUM of Salaries in the table "Employees"\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que20_prblm=Label(que20,text=que20_prblm_text,font=('Arial 12 bold'),padx=20)
que20_prblm.grid(row=1,columnspan=2,sticky='nsew')
que20_solu_label_frame=Frame(que20,bg='#212121') 
Label(que20_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que20_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que20_user_sol=Frame(que20,bg='#212121') 
que20_user_sol.grid_rowconfigure(0,weight=1)
que20_user_sol.grid_rowconfigure(1,weight=1)
que20_user_sol.grid_columnconfigure(0,weight=1) 
que20_user_sol.grid_columnconfigure(1,weight=1) 
que20_user_sol.grid_columnconfigure(2,weight=1) 
que20_user_sol.grid_columnconfigure(3,weight=1) 
que20_user_sol.grid_columnconfigure(4,weight=1) 
que20_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que20_sol1=StringVar()
que20_sol2=StringVar()
que20_sol3=StringVar()
que20_sol1.set("SELECT")
que20_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que20_user_sol,font=('Arial 12 bold'),textvariable=que20_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que20_user_sol,font=('Arial 12 bold'),textvariable=que20_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que20_user_sol,font=('Arial 12 bold'),textvariable=que20_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que20_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(20)).grid(row=0,column=3,padx=5)
Button(que20_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(20)).pack(side=RIGHT,padx=30)
Button(que20_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(20)).pack(side=RIGHT,padx=60)
que20_full_query=Label(que20,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que20_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que20_success_ack=Label(que20,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que20_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que21=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que21.grid_propagate(False) 
que21.grid_columnconfigure(0,weight=1)
que21.grid_columnconfigure(1,weight=1)
que21.grid_rowconfigure(0,weight=1)
que21.grid_rowconfigure(1,weight=1)
que21.grid_rowconfigure(2,weight=1)
que21.grid_rowconfigure(3,weight=1)
que21.grid_rowconfigure(4,weight=1)
que21.grid_rowconfigure(5,weight=1)
que21.grid_rowconfigure(6,weight=1)
que21.grid_rowconfigure(7,weight=1)
que21_header_frame=Frame(que21,bg='#212121',bd=5,relief='sunken') 
Label(que21_header_frame,text=topics_list_ui1[21],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que21_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(21)).pack(side=RIGHT,padx=30)
que21_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que21_prblm_text='''Q: Print the Highest salary in the table "Employees"\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que21_prblm=Label(que21,text=que21_prblm_text,font=('Arial 12 bold'),padx=20)
que21_prblm.grid(row=1,columnspan=2,sticky='nsew')
que21_solu_label_frame=Frame(que21,bg='#212121') 
Label(que21_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que21_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que21_user_sol=Frame(que21,bg='#212121') 
que21_user_sol.grid_rowconfigure(0,weight=1)
que21_user_sol.grid_rowconfigure(1,weight=1)
que21_user_sol.grid_columnconfigure(0,weight=1) 
que21_user_sol.grid_columnconfigure(1,weight=1) 
que21_user_sol.grid_columnconfigure(2,weight=1) 
que21_user_sol.grid_columnconfigure(3,weight=1) 
que21_user_sol.grid_columnconfigure(4,weight=1) 
que21_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que21_sol1=StringVar()
que21_sol2=StringVar()
que21_sol3=StringVar()
que21_sol1.set("SELECT")
que21_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que21_user_sol,font=('Arial 12 bold'),textvariable=que21_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que21_user_sol,font=('Arial 12 bold'),textvariable=que21_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que21_user_sol,font=('Arial 12 bold'),textvariable=que21_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que21_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(21)).grid(row=0,column=3,padx=5)
Button(que21_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(21)).pack(side=RIGHT,padx=30)
Button(que21_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(21)).pack(side=RIGHT,padx=60)
que21_full_query=Label(que21,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que21_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que21_success_ack=Label(que21,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que21_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que22=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que22.grid_propagate(False) 
que22.grid_columnconfigure(0,weight=1)
que22.grid_columnconfigure(1,weight=1)
que22.grid_rowconfigure(0,weight=1)
que22.grid_rowconfigure(1,weight=1)
que22.grid_rowconfigure(2,weight=1)
que22.grid_rowconfigure(3,weight=1)
que22.grid_rowconfigure(4,weight=1)
que22.grid_rowconfigure(5,weight=1)
que22.grid_rowconfigure(6,weight=1)
que22.grid_rowconfigure(7,weight=1)
que22_header_frame=Frame(que22,bg='#212121',bd=5,relief='sunken') 
Label(que22_header_frame,text=topics_list_ui1[22],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que22_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(22)).pack(side=RIGHT,padx=30)
que22_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que22_prblm_text='''Q: Print the Lowest salary in the table "Employees"\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que22_prblm=Label(que22,text=que22_prblm_text,font=('Arial 12 bold'),padx=20)
que22_prblm.grid(row=1,columnspan=2,sticky='nsew')
que22_solu_label_frame=Frame(que22,bg='#212121') 
Label(que22_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que22_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que22_user_sol=Frame(que22,bg='#212121') 
que22_user_sol.grid_rowconfigure(0,weight=1)
que22_user_sol.grid_rowconfigure(1,weight=1)
que22_user_sol.grid_columnconfigure(0,weight=1) 
que22_user_sol.grid_columnconfigure(1,weight=1) 
que22_user_sol.grid_columnconfigure(2,weight=1) 
que22_user_sol.grid_columnconfigure(3,weight=1) 
que22_user_sol.grid_columnconfigure(4,weight=1) 
que22_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que22_sol1=StringVar()
que22_sol2=StringVar()
que22_sol3=StringVar()
que22_sol1.set("SELECT")
que22_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que22_user_sol,font=('Arial 12 bold'),textvariable=que22_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que22_user_sol,font=('Arial 12 bold'),textvariable=que22_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que22_user_sol,font=('Arial 12 bold'),textvariable=que22_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que22_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(22)).grid(row=0,column=3,padx=5)
Button(que22_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(22)).pack(side=RIGHT,padx=30)
Button(que22_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(22)).pack(side=RIGHT,padx=60)
que22_full_query=Label(que22,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que22_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que22_success_ack=Label(que22,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que22_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")

que23=Frame(ui_frame_level1,bd=5,bg='#212121',relief='sunken')
que23.grid_propagate(False) 
que23.grid_columnconfigure(0,weight=1)
que23.grid_columnconfigure(1,weight=1)
que23.grid_rowconfigure(0,weight=1)
que23.grid_rowconfigure(1,weight=1)
que23.grid_rowconfigure(2,weight=1)
que23.grid_rowconfigure(3,weight=1)
que23.grid_rowconfigure(4,weight=1)
que23.grid_rowconfigure(5,weight=1)
que23.grid_rowconfigure(6,weight=1)
que23.grid_rowconfigure(7,weight=1)
que23_header_frame=Frame(que23,bg='#212121',bd=5,relief='sunken') 
Label(que23_header_frame,text=topics_list_ui1[23],font=('Arial 14 bold'),padx=20).pack(side=LEFT,padx=30)
Button(que23_header_frame,text = "View in Detail",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2", command =lambda : view_in_detail(23)).pack(side=RIGHT,padx=30)
que23_header_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
que23_prblm_text='''Q: Print the Average salary in the table "Employees"\nTable: Employees(EmpId int,EmpName Varchar(30),Salary float,Department Varchar(10))'''
que23_prblm=Label(que23,text=que23_prblm_text,font=('Arial 12 bold'),padx=20)
que23_prblm.grid(row=1,columnspan=2,sticky='nsew')
que23_solu_label_frame=Frame(que23,bg='#212121') 
Label(que23_solu_label_frame,text="Solution:",font=('Arial 12 bold'),background='#212121', foreground='White').pack(side=LEFT,padx=30)
que23_solu_label_frame.grid(row=2,columnspan=2,sticky="ew")
que23_user_sol=Frame(que23,bg='#212121') 
que23_user_sol.grid_rowconfigure(0,weight=1)
que23_user_sol.grid_rowconfigure(1,weight=1)
que23_user_sol.grid_columnconfigure(0,weight=1) 
que23_user_sol.grid_columnconfigure(1,weight=1) 
que23_user_sol.grid_columnconfigure(2,weight=1) 
que23_user_sol.grid_columnconfigure(3,weight=1) 
que23_user_sol.grid_columnconfigure(4,weight=1) 
que23_user_sol.grid(row=3,columnspan=2,sticky="nsw")
que23_sol1=StringVar()
que23_sol2=StringVar()
que23_sol3=StringVar()
que23_sol1.set("SELECT")
que23_sol3.set("FROM EMPLOYEES;")
ttk.Entry(que23_user_sol,font=('Arial 12 bold'),textvariable=que23_sol1,width=20).grid(row=0,column=0,padx=30)
ttk.Entry(que23_user_sol,font=('Arial 12 bold'),textvariable=que23_sol2,width=20).grid(row=0,column=1,padx=30)
ttk.Entry(que23_user_sol,font=('Arial 12 bold'),textvariable=que23_sol3,width=20).grid(row=0,column=2,padx=30)
Button(que23_user_sol,text = "Run Query",width=16,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Run_Query(23)).grid(row=0,column=3,padx=5)
Button(que23_solu_label_frame,text = "Reset",width=10,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : Reset(23)).pack(side=RIGHT,padx=30)
Button(que23_solu_label_frame,text = "View Solution",width=15,bg='#5b83ba',font="Arial 12 bold",cursor= "hand2", command =lambda : View_solution(23)).pack(side=RIGHT,padx=60)
que23_full_query=Label(que23,text='',font=('Arial 14 bold'),padx=20,background='#212121', foreground='White')
que23_full_query.grid(row=5,columnspan=2,padx=30,sticky="ew")
que23_success_ack=Label(que23,text='',font=('Arial 14 bold'),background='#212121', foreground='green')
que23_success_ack.grid(row=4,columnspan=2,padx=30,sticky="ew")
""" 
--------------------------------------------------------------------------------------------------------------------------------------------
LEVEL-2
--------------------------------------------------------------------------------------------------------------------------------------------
"""
current_que_l2=0
feedback_list=[]
topic_count_l2={}
crct_count_l2={}
def sample_table():
    global mydb
    mycursor = mydb.cursor()
    full_query=""
    try:
        mycursor.execute("create database if not exists its;")
        mycursor.execute("use its;")
        mycursor.execute("create database if not exists its;")    
        mycursor.execute("drop table if exists office;")
        mycursor.execute("CREATE TABLE office (WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,FIRST_NAME CHAR(25),LAST_NAME CHAR(25),SALARY INT(15),JOINING_DATE DATETIME,DEPARTMENT CHAR(25));")
        mycursor.execute("INSERT INTO office (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES (001, 'Srikanth', 'Arora', 100000, '14-02-20 09.00.00', 'Admin'), (002, 'Uma', 'Rani', 80000, '14-06-11 09.00.00', 'HR'),(003, 'Saif', 'Mughal', 300000, '14-02-20 09.00.00', 'HR'), (004, 'Praveen', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'), (005, 'Manish', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'), (006, 'Prasanth', 'Diwan', 200000, '14-06-11 09.00.00', 'Account'), (007, 'Pavan', 'Kumar', 75000, '14-01-20 09.00.00', 'Account'), (008, 'Suresh', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin'), (009, 'Nethaji', 'Kunda', 40000, '24-09-20 09.00.00', 'Account'),(010, 'Pavan', 'Bhogi', 70000, '28-04-20 09.00.00', 'HR') ;")            
        mydb.commit() 
    except:
        messagebox.showerror("Sorry for inconvenience!","There might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def tableview_l2():
    global mydb
    mycursor = mydb.cursor()
    try:
        mycursor.execute("create database if not exists its;")
        mycursor.execute("use its;")
        mycursor.execute("select * from office")
        data=mycursor.fetchall()
        s=ttk.Style(table_view_level2)
        s.theme_use('classic')
        mod_tree['columns']=('WORKER_ID','FIRST_NAME','LAST_NAME','SALARY','JOINING_DATE','DEPARTMENT')
        #declaring columns
        mod_tree.column('WORKER_ID',width=25,minwidth=75,anchor=CENTER)
        mod_tree.column('FIRST_NAME',width=25,minwidth=75,anchor=CENTER)
        mod_tree.column('LAST_NAME',width=25,minwidth=75,anchor=CENTER)
        mod_tree.column('SALARY',width=30,minwidth=75,anchor=CENTER)
        mod_tree.column('JOINING_DATE',width=65,minwidth=75,anchor=CENTER)
        mod_tree.column('DEPARTMENT',width=25,minwidth=75,anchor=CENTER)
        #assigning heading names
        mod_tree.heading('WORKER_ID',text="WORKER_ID",anchor=CENTER)
        mod_tree.heading('FIRST_NAME',text="FIRST_NAME",anchor=CENTER)
        mod_tree.heading('LAST_NAME',text="LAST_NAME",anchor=CENTER)
        mod_tree.heading('SALARY',text="SALARY",anchor=CENTER)
        mod_tree.heading('JOINING_DATE',text="JOINING_DATE",anchor=CENTER)
        mod_tree.heading('DEPARTMENT',text="DEPARTMENT",anchor=CENTER)
        show_tree(data)
    except mysql.connector.Error as err:
        messagebox.showwarning('Warning!', 'Error No.: {}\nSQL State: {}\n{}'.format(err.errno, err.sqlstate, err.msg))

def show_tree(rows):
    mod_tree.delete(*mod_tree.get_children())
    for i in rows:
        mod_tree.insert('','end',values = i)

def l2_prevtopic():
    global current_que_l2 
    current_que_l2-=1 
    if current_que_l2 < 1:
        messagebox.showinfo("info","No more previous topics to view")
        current_que_l2=0
    level2_que_choice.set(current_que_l2)
    view_task_level2()
    

def l2_nexttopic():
    global current_que_l2 
    current_que_l2+=1 
    if current_que_l2>4:
        messagebox.showinfo("info","No more further topics to view\nYou can start Level II Tutoring")
        current_que_l2=4
    level2_que_choice.set(current_que_l2)
    view_task_level2()
    

def modify_string_level2(s):
    s=s.split(" ")
    result=[] 
    res_comp=""
    for i in range(len(s)):
        if len(res_comp)<=60:
            result.append(s[i])
            res_comp+=s[i]+" "
        else:
            result.insert(len(result)-2,("\n"))
            res_comp=""
    result=" ".join(result)
    while(" \n " in result):
        result=result.replace(" \n ","\n")
    return result 


def view_task_level2():
    #tableview_l2()
    num=level2_que_choice.get()
    if num=="":
        messagebox.showerror("Enter Choice!","Please select any task number")
        return
    elif num.isnumeric():
        num=int(num)
    else:
        messagebox.showerror("Enter Choice!","Please select any task number")
        return
    if num==0:
        default_que_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")
        default_que_level2.tkraise()
        current_que_l2=0
    elif num==1:
        que1_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")
        que1_level2.tkraise()
        current_que_l2=1
    elif num==2:
        que2_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")
        que2_level2.tkraise()
        current_que_l2=2
    elif num==3:
        que3_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")
        que3_level2.tkraise()
        current_que_l2=3
    elif num==4:
        que4_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")
        que4_level2.tkraise()
        current_que_l2=4
    else:
        messagebox.showerror("Sorry for inconvenience!","Please enter task numbers mentioned or,\n\nThere might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def Reset_level2(num):
    if num==1:
        que1_1_1_sol.set("")
        que1_success_ack_l2.configure(text="")
        que1_answer_l2.configure(text="")
        reset_errdesc_level2()
    elif num==2:
        que2_1_1_sol.set("")
        que2_success_ack_l2.configure(text="")
        que2_answer_l2.configure(text="")
        reset_errdesc_level2()
    elif num==3:
        que3_1_1_sol.set("")
        que3_success_ack_l2.configure(text="")
        que3_answer_l2.configure(text="")
        reset_errdesc_level2()
    elif num==4:
        que4_1_1_sol.set("")
        que4_success_ack_l2.configure(text="")
        que4_answer_l2.configure(text="")
        reset_errdesc_level2() 
    else:
        messagebox.showerror("Sorry for inconvenience!","Please enter task numbers mentioned or,\n\nThere might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def View_solution_l2(num):
    if num==1:
        que1_answer_l2.configure(text="Command: update office set salary = 75000 where worker_id = 3;")
        reset_errdesc_level2()
    elif num==2:
        que2_answer_l2.configure(text="Command: alter table office rename column WORKER_ID to W_ID;")
        reset_errdesc_level2() 
    elif num==3:
        que3_answer_l2.configure(text="Command: delete from office where first_name = 'suresh';")
        reset_errdesc_level2() 
    elif num==4:
        que4_answer_l2.configure(text="Command: insert into office values(11,'Ashwin','Agarwal',\n45000,'2014-02-20 09:00:00','Admin');")
        reset_errdesc_level2() 
    else:
        messagebox.showerror("Sorry for inconvenience!","Please enter task numbers mentioned or,\n\nThere might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def Run_Query_l2(num):
    global mydb
    mycursor = mydb.cursor()
    if num==1:
        try:
            query=que1_1_1_sol.get().strip()
            if query=="":
                messagebox.showerror("Empty Query","Please enter the Query")
                return
            mycursor.execute("create database if not exists its;")
            mycursor.execute("use its;")
            mycursor.execute(query)
            mydb.commit()
            reset_errdesc_level2()
            que1_success_ack_l2.configure(text="Well Done! You got it Right")
            que1_answer_l2.configure(text="Command: update office set salary = 75000 where worker_id = 3;")
            mycursor.execute("select * from office")
            data=mycursor.fetchall()
            show_tree(data)  
            for_dicts(crct_count_l2,"Updation")    
        except mysql.connector.Error as err:
                ovl2_errlabel1.configure(text=err.errno)
                ovl2_errlabel2.configure(text=err.sqlstate) 
                ovl2_errlabel3.configure(text=modify_string_level2(err.msg))
        for_dicts(topic_count_l2,"Updation")
    elif num==2:
        try:
            query=que2_1_1_sol.get().strip()
            if query=="":
                messagebox.showerror("Empty Query","Please enter the Query")
                return
            mycursor.execute("create database if not exists its;")
            mycursor.execute("use its;")
            mycursor.execute(query)
            mydb.commit()
            mod_tree.heading('WORKER_ID',text="W_ID",anchor=CENTER)
            reset_errdesc_level2()
            que2_success_ack_l2.configure(text="Well Done! You got it Right")
            que2_answer_l2.configure(text="Command: alter table office rename column WORKER_ID to W_ID;") 
            for_dicts(crct_count_l2,"Rename Column")   
        except mysql.connector.Error as err:
                ovl2_errlabel1.configure(text=err.errno)
                ovl2_errlabel2.configure(text=err.sqlstate) 
                ovl2_errlabel3.configure(text=modify_string_level2(err.msg))
        for_dicts(topic_count_l2,"Rename Column")  

    elif num==3:
        try:
            query=que3_1_1_sol.get().strip()
            if query=="":
                messagebox.showerror("Empty Query","Please enter the Query")
                return
            mycursor.execute("create database if not exists its;")
            mycursor.execute("use its;")
            mycursor.execute(query)
            mydb.commit()
            reset_errdesc_level2()
            que3_success_ack_l2.configure(text="Well Done! You got it Right")
            que3_answer_l2.configure(text="Command: delete from office where first_name = 'suresh';")    
            for_dicts(crct_count_l2,"Deletion")   
        except mysql.connector.Error as err:
                ovl2_errlabel1.configure(text=err.errno)
                ovl2_errlabel2.configure(text=err.sqlstate) 
                ovl2_errlabel3.configure(text=modify_string_level2(err.msg))
        for_dicts(topic_count_l2,"Deletion")
    elif num==4:
        try:
            query=que4_1_1_sol.get().strip()
            if query=="":
                messagebox.showerror("Empty Query","Please enter the Query")
                return
            mycursor.execute("create database if not exists its;")
            mycursor.execute("use its;")
            mycursor.execute(query)
            mydb.commit()
            reset_errdesc_level2()
            que4_success_ack_l2.configure(text="Well Done! You got it Right")
            que4_answer_l2.configure(text="Command: insert into office values(11,'Ashwin','Agarwal',\n45000,'2014-02-20 09:00:00','Admin');")  
            mycursor.execute("select * from office")
            data=mycursor.fetchall()
            show_tree(data) 
            for_dicts(crct_count_l2,"Insertion")  
        except mysql.connector.Error as err:
                ovl2_errlabel1.configure(text=err.errno)
                ovl2_errlabel2.configure(text=err.sqlstate) 
                ovl2_errlabel3.configure(text=modify_string_level2(err.msg))
        for_dicts(topic_count_l2,"Insertion")
    else:
        messagebox.showerror("Sorry for inconvenience!","Please enter task numbers mentioned or,\n\nThere might be a problem with the application,\nwe will work on this issue sorry for the\ninconvenience caused")

def reset_errdesc_level2():
    ovl2_errlabel1.configure(text="")
    ovl2_errlabel2.configure(text="") 
    ovl2_errlabel3.configure(text="")

def performance_graphs_level2():
    try:
        result_dic_l2={}
        for i in topic_count_l2.keys():
            if i not in result_dic_l2:
                if i not in crct_count_l2:
                    result_dic_l2[i]=0
                elif topic_count_l2[i]==crct_count_l2[i]:
                    result_dic_l2[i]=100
                else:
                    result_dic_l2[i]=(crct_count_l2[i]/topic_count_l2[i])*100
        names = list(result_dic_l2.keys())
        values = list(result_dic_l2.values())
        fig_l2 = plt.figure(0)
        fig_l2.canvas.manager.set_window_title('Performance Graph Level II')
        plt.bar(range(len(result_dic_l2)), values, tick_label=names)
        plt.title("Performance Graph Level II")
        plt.ylabel("Accuracy Rate(%)")
        plt.xlabel("Concepts Covered")
        plt.show()
        generate_feedback(result_dic_l2)
    except:
        messagebox.showinfo("Sorry for inconvenience","There might be some issue, as of now\nwe can't able to plot your performance graph!\nWe will work on this issue.")

def generate_feedback(d):
    if len(d)==0:
        return
    feedback_list=[]
    if len(d)<4:
        feedback_list.append("As you have not solved all the questions,\nthis would be a partial feedback for you!\n")
    else:
        feedback_list.append("You are doing great! Here is you feedback for the solved questions")
    for i in d.keys():
        if d[i]==100:
            feedback_list.append("Regarding "+i+", Your have given an outsanding performance")
        elif d[i]>=50:
            feedback_list.append("Regarding "+i+", You are good, You are clear with concept but please practice on writing correct syntax")
        else:
            feedback_list.append("Regarding "+i+", You need to go through the respective topic in Level I")
    contents="\n".join(feedback_list)
    messagebox.showinfo("Feedback",contents)

ui_frame_level2 = Frame(root,bg='#212121',relief='sunken')
ui_frame_level2.grid_columnconfigure(0,weight=3)
ui_frame_level2.grid_columnconfigure(1,weight=2)
ui_frame_level2.grid_rowconfigure(0,weight=1)
ui_frame_level2.grid_rowconfigure(1,weight=1)

que_frame_level2=Frame(ui_frame_level2,bg='#212121',relief='sunken')
table_view_level2=Frame(ui_frame_level2,bg='#212121',bd=5,relief='sunken')
Label(table_view_level2,text="Result",font=('Arial 14 bold'),background='#5b83ba').pack(side="top",fill="both")

output_view_level2=Frame(ui_frame_level2,bg='#212121',bd=5,relief='sunken')

que_frame_level2.grid(row=0,column=0,rowspan=2,sticky="nsew")
table_view_level2.grid(row=0,column=1,sticky="nsew")
output_view_level2.grid(row=1,column=1,rowspan=2,sticky="nsew")
que_frame_level2.grid_propagate(False)
output_view_level2.grid_propagate(False)

que_frame_level2.grid_columnconfigure(0,weight=1)
que_frame_level2.grid_columnconfigure(1,weight=1)
que_frame_level2.grid_rowconfigure(0,weight=1)
que_frame_level2.grid_rowconfigure(1,weight=1)
que_frame_level2.grid_rowconfigure(2,weight=1)
que_frame_level2.grid_rowconfigure(3,weight=1)
que_frame_level2.grid_rowconfigure(4,weight=1)
que_frame_level2.grid_rowconfigure(5,weight=1)
que_frame_level2.grid_rowconfigure(6,weight=1) 
que_frame_level2.grid_rowconfigure(7,weight=1)
que_frame_level2.grid_rowconfigure(8,weight=1)
que_frame_level2.grid_rowconfigure(9,weight=1) 
bottom_frame1_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
Label(bottom_frame1_level2,text='Enter any Task number:',font=('Arial 13 bold'),background='#212121', foreground='white').pack(side="left")
level2_que_choice=StringVar()
ttk.Entry(bottom_frame1_level2,font=('Arial 12 bold'),textvariable=level2_que_choice,width=10).pack(side="left",padx=10)
Button(bottom_frame1_level2,text = "GO",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=view_task_level2).pack(side="left",padx=25)
bottom_frame1_level2.grid(row=8,columnspan=2,sticky="nsew")

bottom_frame_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
bottom_frame_level2.grid_columnconfigure(0,weight=1)
bottom_frame_level2.grid_columnconfigure(1,weight=1)
bottom_frame_level2.grid_columnconfigure(2,weight=1)
bottom_frame_level2.grid_rowconfigure(0,weight=1)
bottom_frame_level2.grid_rowconfigure(1,weight=1)
bottom_frame_level2.grid_propagate(False)
bottom_frame_level2.grid(row=9,columnspan=2,sticky="nsew")

Button(bottom_frame_level2,text = "Previous Topic",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2",command=l2_prevtopic).grid(row=0,rowspan=2,column=0,sticky="nsew")
Button(bottom_frame_level2,text = "Next Topic",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2",command=l2_nexttopic).grid(row=0,rowspan=2,column=2,sticky="nsew")
Button(bottom_frame_level2,text = "Home",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2",command=home).grid(row=0,column=1,sticky="nsew")
Button(bottom_frame_level2,text = "View Feedback",bg='#5b83ba',font="Arial 13 bold", width = 15,cursor= "hand2",command=performance_graphs_level2).grid(row=1,column=1,sticky="nsew")

style1=ttk.Style()
style1.theme_use('classic')
mod_tree=ttk.Treeview(table_view_level2,selectmode='browse')
vsb=ttk.Scrollbar(table_view_level2,orient='vertical')
style1.configure("Vertical.TScrollbar",background="#5b83ba",troughcolor="#212121")
vsb.configure(command=mod_tree.yview)
mod_tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side=RIGHT)
hsb=ttk.Scrollbar(table_view_level2,orient='horizontal')
style1.configure("Horizontal.TScrollbar",background="#5b83ba",troughcolor="#212121")
hsb.configure(command=mod_tree.xview)
mod_tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)
mod_tree['show']='headings'
mod_tree.pack(side=TOP,expand=True,fill="both")

output_view_level2.grid_rowconfigure(0,weight=1)
output_view_level2.grid_rowconfigure(1,weight=1)
output_view_level2.grid_rowconfigure(2,weight=1)
output_view_level2.grid_rowconfigure(3,weight=1)
output_view_level2.grid_rowconfigure(4,weight=1)
output_view_level2.grid_columnconfigure(0,weight=1)
output_view_level2.grid_columnconfigure(1,weight=2)
ovl2_label=Label(output_view_level2,text="Error Description",font=('Arial 14 bold'))
ovl2_label.grid(row=0,column=0,columnspan=2,sticky="new")
Label(output_view_level2,text="Error No:",font=('Arial 10 bold')).grid(row=1,column=0,sticky="nw")
Label(output_view_level2,text="SQL State:",font=('Arial 10 bold')).grid(row=2,column=0,sticky="nw")
Label(output_view_level2,text="Description:",font=('Arial 10 bold')).grid(row=3,column=0,sticky="nw")
ovl2_errlabel1=Label(output_view_level2,text='',font=('Arial 10 bold'),padx=20,background='#212121', foreground='White',justify="left")
ovl2_errlabel2=Label(output_view_level2,text='',font=('Arial 10 bold'),padx=20,background='#212121', foreground='White',justify="left")
ovl2_errlabel3=Label(output_view_level2,text='',font=('Arial 10 bold'),padx=20,background='#212121', foreground='White',justify="left")
ovl2_errlabel1.grid(row=1,column=1,columnspan=2,sticky="nw")
ovl2_errlabel2.grid(row=2,column=1,columnspan=2,sticky="nw")
ovl2_errlabel3.grid(row=3,rowspan=2,column=1,columnspan=2,sticky="nw")

default_que_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
default_que_level2.grid_propagate(False)
default_que_level2.grid_columnconfigure(0,weight=1)
default_que_level2.grid_columnconfigure(1,weight=1)
default_que_level2.grid_rowconfigure(0,weight=1)
default_que_level2.grid_rowconfigure(1,weight=1)
default_que_level2.grid_rowconfigure(2,weight=1)
default_que_level2.grid_rowconfigure(3,weight=1)
default_que_level2.grid_rowconfigure(4,weight=1)
default_que_level2.grid_rowconfigure(5,weight=1)
default_que_level2.grid_rowconfigure(6,weight=1) 
default_que_level2.grid_rowconfigure(7,weight=1)
Label(default_que_level2,text="Tasks",font=('Arial 14 bold')).grid(row=0,column=0,columnspan=2,sticky="new",)
Label(default_que_level2,text='1. Data Modification in table',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=30).grid(row=1,column=0,columnspan=2,sticky="nw",)
Label(default_que_level2,text='2. Altering columns in a table',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=30).grid(row=2,column=0,columnspan=2,sticky="nw",)
Label(default_que_level2,text='3. Deleting rows in a table',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=30).grid(row=3,column=0,columnspan=2,sticky="nw",)
Label(default_que_level2,text='4. Insertion of data in the table',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=30).grid(row=4,column=0,columnspan=2,sticky="nw",)
Label(default_que_level2,text=' <Many tasks would come>\n\n<Application under development>',font=('Arial 13 bold'),background='#212121', foreground='white',).grid(row=4,column=0,columnspan=2,sticky="s")
default_que_level2.grid(row=0,columnspan=2,rowspan=8,sticky="nsew")

que1_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
que1_level2.grid_propagate(False)
que1_level2.grid_columnconfigure(0,weight=1)
que1_level2.grid_columnconfigure(1,weight=1)
que1_level2.grid_rowconfigure(0,weight=1)
que1_level2.grid_rowconfigure(1,weight=1)
que1_level2.grid_rowconfigure(2,weight=1)
que1_level2.grid_rowconfigure(3,weight=1)
que1_level2.grid_rowconfigure(4,weight=1)
que1_level2.grid_rowconfigure(5,weight=1)
que1_level2.grid_rowconfigure(6,weight=1) 
que1_level2.grid_rowconfigure(7,weight=1)
Label(que1_level2,text="1. Data Modification in table",font=('Arial 14 bold')).grid(row=0,column=0,columnspan=2,sticky="new",)
Label(que1_level2,text='Q. Change the salary to 75,000/- whose worker Id is 3 in table office',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=10).grid(row=1,column=0,columnspan=2,sticky="nw",)
que1_1_1_sol=StringVar()
ttk.Entry(que1_level2,font=('Arial 12 bold'),textvariable=que1_1_1_sol).grid(row=2,column=0,columnspan=2,sticky="new",padx=10)
que1_success_ack_l2=Label(que1_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='green')
que1_answer_l2=Label(que1_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='white')
que1_success_ack_l2.grid(row=4,column=0,columnspan=2)
que1_answer_l2.grid(row=5,column=0,columnspan=2)
Button(que1_level2,text = "Run",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Run_Query_l2(1)).grid(row=3,column=1,sticky="e",padx=10)
Button(que1_level2,text = "Reset",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Reset_level2(1)).grid(row=3,column=0,sticky="w",padx=10)
Button(que1_level2,text = "View Solution",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : View_solution_l2(1)).grid(row=3,column=0,sticky="e",padx=10)

que2_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
que2_level2.grid_propagate(False)
que2_level2.grid_columnconfigure(0,weight=1)
que2_level2.grid_columnconfigure(1,weight=1)
que2_level2.grid_rowconfigure(0,weight=1)
que2_level2.grid_rowconfigure(1,weight=1)
que2_level2.grid_rowconfigure(2,weight=1)
que2_level2.grid_rowconfigure(3,weight=1)
que2_level2.grid_rowconfigure(4,weight=1)
que2_level2.grid_rowconfigure(5,weight=1)
que2_level2.grid_rowconfigure(6,weight=1) 
que2_level2.grid_rowconfigure(7,weight=1)
Label(que2_level2,text="2. Altering columns in a table",font=('Arial 14 bold')).grid(row=0,column=0,columnspan=2,sticky="new",)
Label(que2_level2,text='Q. Chagne column "WORKER_ID" to "W_ID" in table Office',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=10).grid(row=1,column=0,columnspan=2,sticky="nw",)
que2_1_1_sol=StringVar()
ttk.Entry(que2_level2,font=('Arial 12 bold'),textvariable=que2_1_1_sol).grid(row=2,column=0,columnspan=2,sticky="new",padx=10)
que2_success_ack_l2=Label(que2_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='green')
que2_answer_l2=Label(que2_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='white')
que2_success_ack_l2.grid(row=4,column=0,columnspan=2)
que2_answer_l2.grid(row=5,column=0,columnspan=2)
Button(que2_level2,text = "Run",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Run_Query_l2(2)).grid(row=3,column=1,sticky="e",padx=10)
Button(que2_level2,text = "Reset",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Reset_level2(2)).grid(row=3,column=0,sticky="w",padx=10)
Button(que2_level2,text = "View Solution",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : View_solution_l2(2)).grid(row=3,column=0,sticky="e",padx=10)

que3_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
que3_level2.grid_propagate(False)
que3_level2.grid_columnconfigure(0,weight=1)
que3_level2.grid_columnconfigure(1,weight=1)
que3_level2.grid_rowconfigure(0,weight=1)
que3_level2.grid_rowconfigure(1,weight=1)
que3_level2.grid_rowconfigure(2,weight=1)
que3_level2.grid_rowconfigure(3,weight=1)
que3_level2.grid_rowconfigure(4,weight=1)
que3_level2.grid_rowconfigure(5,weight=1)
que3_level2.grid_rowconfigure(6,weight=1) 
que3_level2.grid_rowconfigure(7,weight=1)
Label(que3_level2,text="3. Deleting rows in a table",font=('Arial 14 bold')).grid(row=0,column=0,columnspan=2,sticky="new",)
Label(que3_level2,text='Q. Delete data whose first name is "Suresh"',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=10).grid(row=1,column=0,columnspan=2,sticky="nw",)
que3_1_1_sol=StringVar()
ttk.Entry(que3_level2,font=('Arial 12 bold'),textvariable=que3_1_1_sol).grid(row=2,column=0,columnspan=2,sticky="new",padx=10)
que3_success_ack_l2=Label(que3_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='green')
que3_answer_l2=Label(que3_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='white')
que3_success_ack_l2.grid(row=4,column=0,columnspan=2)
que3_answer_l2.grid(row=5,column=0,columnspan=2)
Button(que3_level2,text = "Run",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Run_Query_l2(3)).grid(row=3,column=1,sticky="e",padx=10)
Button(que3_level2,text = "Reset",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Reset_level2(3)).grid(row=3,column=0,sticky="w",padx=10)
Button(que3_level2,text = "View Solution",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : View_solution_l2(3)).grid(row=3,column=0,sticky="e",padx=10)

que4_level2=Frame(que_frame_level2,bg='#212121',bd=5,relief='sunken')
que4_level2.grid_propagate(False)
que4_level2.grid_columnconfigure(0,weight=1)
que4_level2.grid_columnconfigure(1,weight=1)
que4_level2.grid_rowconfigure(0,weight=1)
que4_level2.grid_rowconfigure(1,weight=1)
que4_level2.grid_rowconfigure(2,weight=1)
que4_level2.grid_rowconfigure(3,weight=1)
que4_level2.grid_rowconfigure(4,weight=1)
que4_level2.grid_rowconfigure(5,weight=1)
que4_level2.grid_rowconfigure(6,weight=1) 
que4_level2.grid_rowconfigure(7,weight=1)
Label(que4_level2,text="4. Insertion of data in the table",font=('Arial 14 bold')).grid(row=0,column=0,columnspan=2,sticky="new",)
Label(que4_level2,text='Q. Insert data into table office Data:(worker_id=11,\nfirst_name="Ashwin",last_name="Agarwal",salary=45000,\njoining_date="2014-02-20 09:00:00",Department="Admin")',font=('Arial 13 bold'),background='#212121', foreground='white',justify="left",padx=10).grid(row=1,column=0,columnspan=2,sticky="nw",)
que4_1_1_sol=StringVar()
ttk.Entry(que4_level2,font=('Arial 12 bold'),textvariable=que4_1_1_sol).grid(row=2,column=0,columnspan=2,sticky="new",padx=10)
que4_success_ack_l2=Label(que4_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='green')
que4_answer_l2=Label(que4_level2,text='',font=('Arial 13 bold'),background='#212121', foreground='white')
que4_success_ack_l2.grid(row=4,column=0,columnspan=2)
que4_answer_l2.grid(row=5,column=0,columnspan=2)
Button(que4_level2,text = "Run",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Run_Query_l2(4)).grid(row=3,column=1,sticky="e",padx=10)
Button(que4_level2,text = "Reset",width=10,bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : Reset_level2(4)).grid(row=3,column=0,sticky="w",padx=10)
Button(que4_level2,text = "View Solution",bg="#5b83ba",font="Arial 13 bold",cursor= "hand2",command=lambda : View_solution_l2(4)).grid(row=3,column=0,sticky="e",padx=10)


root.mainloop()