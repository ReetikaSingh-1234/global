from django.shortcuts import render,HttpResponse
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

def show(request):
    return render(request,'show.html')
# Create your views here.
def login(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="rootuser",passwd="Reetika@13",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
        
            if key=="email":
                em=value
            if key=="password":
                pwd=value 
                
        c="select * from adminsignup where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'show.html') 
        else:
            return render(request,"show.html")
             
    return render(request,"adminlogin.html")
                       
  