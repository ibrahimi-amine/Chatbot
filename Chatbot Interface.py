from tkinter import *
from modell import chat
import pymysql





def create_projects( nom_m,titre_p, description):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #definir le premier cursor
    cursor_1 = conn.cursor()
    
    #definir la premiere requete
    query_1 =  "select id_m from membre where nom_m = %s"
    
    #executer la premiere requete SQL
    cursor_1.execute(query_1,nom_m)
    
    #extrait les données recues
    #data est une table de deux colonnes, id_m et nom_m
    data= cursor_1.fetchall()
        
    #definir le deuxiem cursor
    cursor_2 = conn.cursor()
    
    #Definir la deuxieme requete SQL
    query_2 =  "insert into projet (id_m,titre_p,description) values (%s,%s,%s);"
    
    #Executer la deuxieme requete SQL      
    cursor_2.execute(query_2, (data[0],titre_p,description))
    
           
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()

def show_projects(titre_p):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée    
    query = "select t.titre_t as 'Titre', t.statut as 'Etat de la tâche', m.nom_m as 'Affectée à' from projet p, tache t, membre m where m.id_m=p.id_m and p.id_p=t.id_p and p.titre_p= %s ;"
    
    #Execute la requete
    cursor.execute(query, titre_p)
    
    #Naviguer dans les données extraites
    data= cursor.fetchall()
    #Afficher les données
    L=''
    for w in data:
        D="\n"+"Tâche        : "+w[0]+"\n"+"Avancement    : "+w[1]+"\n"+"Tâche affectée à : "+w[2]+"\n"+"-------------------------------"
        L=L+D
    return L


def show_projet2(titre_p):
     #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query_1 = "select titre_p, description from projet where titre_p = %s"    
    
    #Execute la requete 1
    cursor.execute(query_1, titre_p)

    
    #Naviguer dans les données extraites
    data= cursor.fetchall()

    return ("\n"+"Titre                   : "+data[0][0]+"\n"+"Description du Projet   : "+data[0][1])      
        


def delete_projects(titre_p):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query =  """delete from projet where titre_p= %s """
 
    #Execute la requete
    cursor.execute(query, titre_p)    
        
    #Acccept le changement
    conn.commit()
 
    #Fermer le cursor
    cursor.close()
    
    #Fermer la connection avec la base de donnees
    conn.close()    

def create_tache(titre_t,desc_t,statut,nom_m,titre_p):
    
    #Se connecter à la base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Définir un cursor
    cursor_1 = conn.cursor()
    cursor_2 = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query_1 = " select p.id_p, p.titre_p, m.id_m, m.nom_m from projet p, membre m where m.id_m=p.id_m and nom_m = %s and titre_p = %s ; "
    
    #Executer la requete SQL
    cursor_1.execute(query_1,(nom_m,titre_p))    
    
    
    data= cursor_1.fetchall()
    

    
    query_2 = " insert into tache (titre_t,desc_t,statut,id_m, id_p) values (%s,%s,%s,%s,%s);"
    
    #Executer la requete SQL
    
    cursor_2.execute(query_2, (titre_t,desc_t,statut,data[0][2],data[0][0]))
    
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()
    
def show_tache(titre_p,titre_t):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query = "select p.titre_p, t.titre_t, m.nom_m, t.desc_t from projet p, tache t, membre m where p.id_p = t.id_p and m.id_m=p.id_m and p.titre_p =%s and t.titre_t = %s "    
    
    #Execute la requete 1
    cursor.execute(query, (titre_p,titre_t))
    
    print("Query well executed")
        
    #Naviguer dans les données extraites
    data= cursor.fetchall()
    
    
    print("\n")
    
    #Afficher les données
    for w in data:
        return("\n"+"Projet           : "+w[0]+"\n"+"Nom de la tâche  : "+w[1]+"\n"+"Responsable      : "+w[2]+"\n"+"Description      : "+w[3]+"\n")
        

    
def delete_tache(titre_p,titre_t):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Définir un cursor
    cursor = conn.cursor()
    
    #Définir la requete SQL souhaitée
    query = """ DELETE tache FROM tache INNER JOIN projet ON projet.id_p = tache.id_p WHERE tache.titre_t = %s and projet.titre_p = %s; """
  
    #Executer la requete
    cursor.execute(query,(titre_t,titre_p))
    
    #Acccepter le changement
    conn.commit()
    
    #Fermer la connexion avec la base de données
    conn.close()
    
    
    
def add_membre(nom_m,email_m,password_m):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query =  """insert into membre (nom_m,email_m,password_m) values (%s,%s,%s);"""
    
    #Executer la requete SQL
    cursor.execute(query, (nom_m,email_m,password_m))
    
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()
    
def show_members(nom_m):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query = "select nom_m, email_m, id_m from membre where nom_m = %s "    
    
    #Execute la requete 1
    cursor.execute(query, nom_m)
    
    #Naviguer dans les données extraites
    data= cursor.fetchall()

    
    #Afficher les données
    for w in data:
        return("\n"+"Nom        : "+w[0]+"\n"+"E_mail      : "+w[1]+"\n"+"id_m      : "+str(w[2])+"\n"+"-------------------------------")




root =Tk()

txt=Text(root,width=70)
txt.grid(row=0,column=0)

e=Entry(root,width=55)
e.grid(row=1,column=0)

txt.insert(END,"-> Start talking with the bot \n-> (type quit to stop)!"+"\n")


    
delete_project=0    
create_project=0
show_project=0
project=[]

create_task=0
show_task=0
delete_task=0
task=[]
show_t=[]
delete_t=[]

delete_member=0    
create_member=0
show_member=0
member=[]


def quitt(self):
    self.destroy()
    exit()
    
def send():
    global create_project
    global show_project
    global delete_project
    global project
    
    global create_task
    global show_task
    global delete_task
    global task
    global show_t
    global delete_t
    
    global delete_member
    global create_member
    global show_member
    global member
    
    
    inp=e.get()
    if inp =="quit":
        quitt(root)
    send= "->User :" + inp
    txt.insert(END,send+"\n")
    e.delete(0,END)
    
    chatbot_response=chat(inp)
    
        #################################################################
    
    ###############################  create a new ^project
    if chatbot_response[1]=="create_projet":
        create_project=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    
    if create_project==1:        #get the project name and ask for the description 
        txt.insert(END,"->Trello chatbot :"+"add the descreption of the "+inp+" project"+"\n")
        project.append(inp)
        create_project=2
        return 
    
    if create_project==2:        #get the project descreption and ask for the chef
        txt.insert(END,"->Trello chatbot :"+"add the name of the chef of the "+project[0]+" project"+"\n")
        project.append(inp)
        create_project=3
        return
    if create_project==3:
        project.append(inp)
        create_projects(project[2],project[0],project[1])
        txt.insert(END,"->Trello chatbot :The project has been added succesfully"+"\n")
        create_project=0
        return

    
        ###############################  show a ^project
    if chatbot_response[1]=="show_project":
        show_project=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    if show_project==1:
        txt.insert(END,"->Trello chatbot :"+show_projet2(inp)+"\n"+show_projects(inp)+"\n")
        show_project=0
        return
       
        ###############################  delete a ^project
    if chatbot_response[1]=="delete_project":
        delete_project=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    if delete_project==1:
        delete_projects(inp)
        txt.insert(END,"->Trello chatbot : Project deleted succesfully"+"\n")
        delete_project=0
        return
    
        #################################################################
        
     ###############################  create a new ^task titre_t,desc_t,statut,nom_m,titre_p
    if chatbot_response[1]=="create_task":
        create_task=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    
    if create_task==1:        #get the task name and ask for the description 
        txt.insert(END,"->Trello chatbot :"+"add the descreption of the "+inp+" task"+"\n")
        task.append(inp)
        create_task=2
        return 
    if create_task==2:        #get the task descreption and ask for the status
        txt.insert(END,"->Trello chatbot :"+"add the status of the "+task[0]+" task"+"\n")
        task.append(inp)
        create_task=3
        return
    if create_task==3:        #get the task status and ask for the project that's belong to
        txt.insert(END,"->Trello chatbot :"+"add the project in wich the "+task[0]+" task belong to"+"\n")
        task.append(inp)
        create_task=4
        return
    if create_task==4:        #get the project and ask for the member who is in charge of the task
        txt.insert(END,"->Trello chatbot :"+"add the member who is in charge of the "+task[0]+" task"+"\n")
        task.append(inp)
        create_task=5
        return
    if create_task==5:
        task.append(inp)
        create_tache(task[0],task[1],task[2],task[4],task[3])
        txt.insert(END,"->Trello chatbot :The task has been added succesfully"+"\n")
        create_task=0
        return
    
    
    ###############################  show a ^task
    if chatbot_response[1]=="show_task":
        show_task=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    if show_task==1:
        show_t.append(inp)
        txt.insert(END,"->Trello chatbot :Add the project name that contains this task"+"\n")
        show_task=2
        return
    if show_task==2:
        show_t.append(inp)
        txt.insert(END,"->Trello chatbot :"+show_tache(show_t[1],show_t[0])+"\n")
        show_task=0
        return
    
    ###############################  delete a ^task
    if chatbot_response[1]=="delete_task":
        delete_task=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    if delete_task==1:
        delete_t.append(inp)
        txt.insert(END,"->Trello chatbot : add the project name that contains this task"+"\n")
        delete_task=2
        return
    if delete_task==2:
        delete_t.append(inp)
        delete_tache(delete_t[1],delete_t[0])
        txt.insert(END,"->Trello chatbot : Task deleted succesfully"+"\n")
        delete_task=0
        return
    
        #################################################################
        
         ###############################  create a new ^member
    if chatbot_response[1]=="create_member":
        create_member=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    
    if create_member==1:        #get the member name and ask for the email
        txt.insert(END,"->Trello chatbot :"+"add the email of the "+inp+" member"+"\n")
        member.append(inp)
        create_member=2
        return 
    
    if create_member==2:        #get the member email and ask for the password
        txt.insert(END,"->Trello chatbot :add the password of the "+member[0]+" member"+"\n")
        member.append(inp)
        create_member=3
        return
    if create_member==3:
        member.append(inp)
        add_membre(member[0],member[1],member[2])
        txt.insert(END,"->Trello chatbot :The member has been added succesfully"+"\n")
        create_member=0
        return
    
    ###############################  show a ^member
    if chatbot_response[1]=="show_member":
        show_member=1
        txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")
        return 
    if show_member==1:
        txt.insert(END,"->Trello chatbot :"+show_members(inp)+"\n")
        show_member=0
        return
        
    txt.insert(END,"->Trello chatbot :"+chatbot_response[0]+"\n")

print(create_project)      

    
    
send=Button(root,text="send",fg="red",width=10,command=send).grid(row=1,column=1)


root.title("Trello Chatbot")
root.mainloop()




