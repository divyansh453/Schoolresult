print("**THIS IS THE PROJECT OF COMPUTER SCIENCE(PYTHON) BY DIVYANSHU RANA & NAVNEET MANI OF CLASS-XII(SESSION:-2020-21)**")
print('''
                **INTRODUCTION**
NAME-DIVYANSHU RANA                NAME-NAVNEET MANI
                         AND
ROLL NUMBER-03                     ROLL NUMBER-14
''')
print("Welcome,Now you can check sql data without opening 'Mysql'")
h=input("Enter host's name:")
u=input("Enter user's name:")
p=input("Enter your password:")
d=input("Enter your class(Use Roman numbers ):")
def changer(c):
    global d
    d=c
    print(d)
    runner(h,u,p,d)
def thank():
    print("*******Thankyou for using program if you want to do more operations then you can run it again*****")
    f=input('If you want to run it again then enter<run> otherwise press ENTER key:')
    f=f.lower()
    if f=='run':
        nt=input("If you want to change class then enter<1> otherwise press ENTER key :")
        if nt=='1':
            gr=input("Enter your class(in roman numbers):")
            changer(gr)
        else:
            runner(h,u,p,d)
    else:
        print('Bye')
def runner(h,u,p,d):
    def project(pt):
        cobject.execute(pt)
        data=cobject.fetchall()
        for r in data:
            print(r)
    def projectu(pt):
        cobject.execute(pt)
        nm.commit()
    def ranks():
        dg=('select ' +d+'_english.Roll_no,'+d+'_english.Student_Name,('+d+'_cs.Marks+'+d+'_chemistry.Marks+'+d+'_physics.Marks+'+d+'_maths.Marks+'+d+'_biology.Marks+')
        he=(d+'_english.Marks+'+d+'_hindi.Marks)as Total_Marks,(('+d+'_cs.Percentage+'+d+'_chemistry.Percentage+'+d+'_physics.Percentage+'+d+'_maths.Percentage+')
        li=(d+'_biology.Percentage+'+d+'_english.Percentage+'+d+'_hindi.Percentage)/5) as Percentage from '+d+'_cs,'+d+'_physics,'+d+'_chemistry,'+d+'_maths,')     
        be=(d+'_biology,'+d+'_english,'+d+'_hindi where '+d+'_chemistry.Roll_no='+d+'_cs.Roll_no and '+d+'_chemistry.Roll_no='+d+'_maths.Roll_no and ')
        bo=(d+'_chemistry.Roll_no='+d+'_physics.Roll_no and '+d+'_chemistry.Roll_no='+d+'_biology.Roll_no and '+d+'_chemistry.Roll_no='+d+'_english.Roll_no and ')
        hg=(d+'_chemistry.Roll_no='+d+'_hindi.Roll_no order by Percentage desc')
        cd=dg+he+li+be+bo+hg
        lk=d.upper()
        print("########################################  RESULT OF CLASS-"+lk+" WITH THE RANK OF STUDENTS  #######################################")
        print("Sequence of following tuples--->Roll_no,Student_name,Marks,Percentage")
        project(cd)
        cobject.execute(cd)
        datar=cobject.fetchmany(3)
        print("Toppers of the class "+lk+" are:")
        for i in range(3):
            cg=datar[i]
            print("Rank "+str(i+1)+":",cg[1])  
        hy=input("")
    def copy(av):
        av.lower()
        if av=='maths':
            ny='biology'
        elif av=='biology':
            ny='maths'
        elif av=='cs':
            ny='hindi'
        elif av=='data':
            ny='cs'
        mb=[]
        mb1=[]
        mb2=[]
        mb3=[]
        pf=f+s+av
        fp=f+s+ny
        cobject.execute(pf)
        tg=cobject.fetchall()
        cobject.execute(fp)
        gt=cobject.fetchall()
        for ty in tg:
            qf=ty
            rno1=qf[0]
            mb.append(rno1)
        for yt in gt:
            fq=yt
            rno=fq[0]
            mb1.append(rno)
            rnoo=str(rno)
            name=fq[1]
            mb2.append(name)
            
        for ar in mb1:
            if ar not in  mb:
                ar=str(ar)
                hh="INSERT INTO `"+d+"_"+av+"` (`Roll_no`,`Marks`,`Percentage`) VALUES ("+ar+",0,0)"
                projectu(hh)
        
        hy="select Roll_no from  "+d+"_"+av+ " where Student_name is null"
        cobject.execute(hy)
        hr=cobject.fetchall()
        mb4=[]
        for hu in hr:
            for tu in hu:
                mb4.append(tu)
                htc="select Student_name from "+d+"_"+ny+" where Roll_no="+(str(tu))
                cobject.execute(htc)
                hur=cobject.fetchall()
                for tuc in hur:
                    for huc in tuc:
                        mb3.append(huc)
        for i in range(len(mb4)):
            name=mb3[i]
            rno=(mb4[i])
            fg="update  "+d+"_"+av+" set Student_name='"+name+"' where Student_name is null and Roll_no="+str(rno)
            projectu(fg)
        
    def create():
        print('List of  available tables:')
        pt="show tables"
        project(pt)
        print("Your table will be created as [class(in roman number)_<subject>] and you have to enter only subject in next option...")
        ss=input("ENTER SUBJECT:")
        ss=ss.upper()
        if ss==" ":
            print("INVALID INPUT!!")
        elif ss=="DETAILS":
            st='create table '+d+'_'+ss+' (Roll_no integer not null primary key,DOB date not null,Father_name varchar(25) not null,'
            sc='Address varchar(100) not null)'
            obc=st+sc
            projectu(obc)
            print("Your table is successfully created.")
            print("Now tables are:")
            project(pt)
            thank()
        else:    
            st='create table '+d+'_'+ss+' (Roll_no integer not null primary key,Student_name varchar(25),Marks integer ,Percentage decimal)'
            projectu(st)
            print("Your table is successfully created.")
            print("Now tables are:")
            project(pt)
            thank()
    import mysql.connector as dr
    nm=dr.connect(host=h,user=u,passwd=p,database=d)
    if nm.is_connected():
        print("You are successfully connected to database of class",d,'.')
        cobject=nm.cursor()
        print("If you want to create class database and subject table then enter<create>:")
        print("If you want to check only ranks then enter<ranks>:")
        print("To check,insert,delete or update data,press ENTER key:")
        kt=input("")
        kt=kt.lower()
        if kt=='ranks' or kt=='rank':
            try:
                ranks()
                thank()
            except:
                print("Data of subjects is not filled yet..")
                thank()
        elif kt=='create':
            print("If you want to create database then enter <db> and if you want to create table then enter <tb>:")
            fe=input("")
            fe=fe.lower()
            if fe=='db':
                print("Available databases:")
                dd='show databases'
                project(dd)
                ar=input("Enter the class for which you want to create database:")
                st="create database "+ar
                projectu(st)
                print("Database created successfully...")
                rf=input("If you want to use this database now then enter<1> otherwise press ENTER key:")
                if rf=='1':
                    changer(ar)  
                else:
                    thank()
            elif fe=='tb':
                create()
            else:
                print('INVALID INPUT!!')
                thank()
        else:
            print('Subject names along with classes are given below you can choose according to your need:')
            pt="show tables"
            project(pt)
            print("NOTE:-You have to enter subject and class according to above names otherwise program will not work.")
            print("If you want to check  details then you can also enter details at the place of subject.")
            p=input("Enter your subject:")
            p=p.lower()
            f=("select* from ")
            s=d+'_'
            try:
                copy(p)
            except:
                print("Sorry there is some problem ,Please create table of all subjects. ")
            print("If you have been entered <details> as your subject then you cannot choose <3> and <1>only for next entry,otherwise you will not get desired result.")
            print("To check subject details enter<1>")
            print("To check personal details enter<2>")
            print("To check whole details enter<3>")
            hj=input("")
            if hj=='1':
                if p=="details":
                    print("INVALID OPTION!!,you cannot do your desired operation.")
                else:
                    f=("select* from ")
                    s=d+'_'
                    ph=f+s+p+" where marks>0"
                    print("Data of Subject","'",p,"'""of Class",d)
                    print("Sequence of given tuples is:-Roll_no,Student_name,Marks,Percentage")
                    project(ph)
            elif hj=='2':
                print("Sequence of given tuples is:-Roll_no,DOB[YYYY-MM-DD],Father_name,Address:")
                ad="select*from "+d+"_"+"details"
                project(ad)
            elif hj=='3':
                if p=="details":
                    print("INVALID OPTION!!,you cannot do your desired operation.")
                else:
                     print("Sequence of given tubles is:-Student_name,Father_name,DOB[YYYY-MM-DD],Marks,Percentage,Address ")
                     af=("select Student_name,Father_name,DOB,Marks,Percentage,Address from "+d+"_"+p+","+d+"_details where "+d+"_"+p+".Roll_no="+d+"_details.Roll_no and Marks>0;")
                     project(af)
            else:
                print("INVALID INPUT!!")
            print("If you want to insert more data then enter <insert>:")
            print("If you want to update data then enter<update>:")
            print("If you want to delete any record then enter<delete>")
            print("If you want to check only result then press ENTER key.")  
            k=input("")
            k=k.lower()
            if k=='insert':
                nh=int(input("Enter the number of student for which you want to insert your data:"))
                print("If you have been choosed <details> as your subject then you can only enter<1> in next option")
                print("If subject details are complete and you want to insert personal details only then enter<1>:-")
                print("If personal details are completed and you want to insert subject details only then enter<2>:-")
                print("If you want to insert both personal and subject details then enter<3>:-")
                lk=input("")
                if lk=='2' or lk=='3':
                    if p=="details":
                        print("INVALID OPTION!!,you cannot do your desired operation.")
                        thank()
                    else:
                        print("You are entering the data of",p)
                        print("WARNING!!:-REPEATITION OF ROLL NUMBER IS NOT ALLOWED OTHERWISE YOU WILL FACE AN ERROR!!!.")
                        for i in range(nh):
                            m=int(input('Enter Roll number.:-'))
                            n=input("Enter Student's Name:-")
                            b=int(input("Enter Marks:-"))
                            p.lower()
                            z=0
                            if p=='cs' or p=='physics' or p=='chemistry' or p=='biology':
                                z=70
                            if p=='maths' or p=='english' or p=='hindi':
                                z=80
                            j=(b/z)*100
                            n=n.title()
                            dt=(m,n,b,j)
                            h=str(dt)
                            f=("select* from ")
                            s=d+'_'
                            ph=f+s+p+" where marks>0" 
                            st="insert into "+d+"_"+p+" values"
                            s=st+h
                            if z==70 and b<=70:
                                projectu(s)
                            elif z==80 and b<=80:
                                projectu(s)
                            elif b>70 or b>80:
                                print("Sorry you filled more marks than maximum marks.")
                            print("Now,data of Subject",p,"of Class",d,'.')
                            print("Sequence of following tuples---->Roll_no,Student_name,Marks,Percentage.")
                            project(ph)
                            if lk=='1':
                            	thank()
                            else:
                            	continue
                if lk=='1' or lk=='3':
                    for i in range(nh):
                        m=int(input('Enter Roll number.:-'))
                        v=input("Enter date of birth as[YYYY-MM-DD];-")
                        jj=input("Enter Father's Name:- ")
                        b=input("Enter Address of student:-")
                        jj=jj.title()
                        dt=(m,v,jj,b)
                        h=str(dt)
                        sc="insert into "+d+"_"+"details"+" values"
                        sg=sc+h
                        projectu(sg)
                        print("Now,details of student of class",d)
                        print("Sequence of following tuples---->Roll_no,DOB[YYYY-MM-DD],Father's name,Address")
                        ad='select*from '+d+'_details'
                        project(ad)
                    thank()
                else:
                    thank()
            elif k=='update':
                print("Fields--->Roll_no,Student_name,DOB,Marks,Percentage,Father_name,Address")
                print("NOTE:-If you are updating a string then you have to write the change as<'string'>.")
                print("If you want to change data of one student then enter<1>:")
                print("If you want to change marks of every student then enter<2>:")
                pu=(input(""))
                if pu=='1':
                    print("You are updating the data of",p)
                    mu=(input("Enter Student's roll number:"))
                    nu=input("Select the field you want to change:")
                    cu=input("Enter the change you want:")
                    su="update "+d+'_'+p+" set "+nu+"="+cu+" where "+" Roll_no"+"="+mu
                    projectu(su)
                    print("Successfully updated")
                    print("Now data is:")
                    pt='select*from '+d+'_'+p
                    project(pt)
                    thank()
                elif pu=='2':
                    if p=='details':
                        print('''INVALID OPTION!!,this facility is not available for updating details,if you want to do so then you have to run it again by entering
<run> in the end of program.''')
                    else:
                        np=input("Enter the marks you want to change:")
                        print("If you want to reduce then enter (-):")
                        print("If you want to add then enter (+):")
                        print("If you want to multiply or divide marks then enter (*) or(/) respectively")
                        hu=input("")
                        hk=input("Enter the estimation:")
                        sr="update "+d+'_'+p+" set "+"Marks"+"="+"Marks"+hu+hk+" where "+"Marks"+"="+np+" and Marks>0"
                        print(sr)
                        projectu(sr)
                        print("Sucessfully updated")
                        print("Now data is:")
                        pt='select*from '+d+'_'+p+' where Marks>0'
                        project(pt)
                        thank()
                else:
                    print("INVALID INPUT!!")
                    thank()
            elif k=='delete':
                ju=int(input("Enter the number of students for which you want to delete data:"))
                for i in range(ju+1):
                    rr=input("Enter the roll number of student:")
                    print("To delete subject details enter<1>:")
                    print("To delete personal details enter<2>:")
                    print("To delete whole details enter<3>:")
                    dd=input("")
                    if dd=='1':
                        print("Data will be deleted from",p)
                        fg='delete from '+d+'_'+p+' where Roll_no='+rr
                        projectu(fg)
                        print("Record is deleted.")
                        thank()
                    elif dd=='2':
                        fg='delete from '+d+'_details where Roll_no='+rr
                        projectu(fg)
                        print("Record is deleted")
                        thank()
                    elif dd=='3':
                        print("Data will be deleted from",p)
                        fg='delete from '+d+'_'+p+' where Roll_no='+rr
                        gg='delete from '+d+'_details where Roll_no='+rr
                        projectu(fg)
                        projectu(gg)
                        print("Record is deleted")
                        thank()
                    else:
                        print("INVALID INPUT!!")
                        thank()   
                
            else:
                    print("********************************************")
                    try:
                        ranks()
                        thank()
                    except:
                        print("Data of subjects is not filled yet..")
                        thank()
    else:
        print("Sorry for inconvience")
runner(h,u,p,d)
#END OF PROGRAM.
