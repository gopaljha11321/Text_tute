# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render 
def index(request):
    return HttpResponse('''<h1>gopal jha is here</h1>
    <h2><a href="/learning1">Learning 1</a></h2>
    <h2><a href='/boostrap'>Learn boostrap </a></h2>
    ''')
def learning1(request):
    # return HttpResponse('''<h1>gopal jha is here</h1> <h2>hello everyone here</h2> <a href="https://gopaljha11321.github.io/profile/">gopajha</a>
    # <h1><a href="https://gopaljha11321.github.io/fp_Vitality/">vitality</a><h1 >
    # ''');
     
     #render are use for trnasfer the data from main python to html file on other side we use {{}} this symbol 
     #rendor have three parameter: 1. request 2. path 3. variable
    
    a={'name1':"gopal",'name2':"ravi"}
    return render(request,'index.html',a);

def removepunc(request):

    #get data from html page by using request.GET.get() function in python
    #post data from html page by using request.POST.get() function in python when ever we use post we have to write {% csrf_token %} on form section on html

    t1=request.POST.get('text','default')
    t2=request.POST.get('removepunch','off')
    t3=request.POST.get('upperCase','off')
    t4=request.POST.get('nlr','off')
    print(t1);
    out=t1
    if t2=="on":
        specil_key=["!","@","#","$","%","^","&","*","(",")","_","+","{","}",":","<",">",">","<","?","|",",",".",";","'","[","]","/","-","=",]
        result=""
        for i in t1:
            if i not in specil_key:
                result+=i;
        out=result;
        
    if(t3=="on"):
        out=out.upper()
    if(t4=="on"):
        result=""
        for i in out:
            if(i !="\n"):
                result+=i;
            else:
                break;
        out=result;
    if((t2=="off") and (t3=="off") and t4=="off"):
        test1={ 
        "word":t1,
        "result":"Select checkbox"
        }
        return render(request,'removePunch.html',test1)
    test1={ 
        "word":t1,
        "result":out
        }
    return render(request,'removePunch.html',test1)
        
    
def contact(request):
    return HttpResponse('''8745977703  
    <a href='/'>back</a>
    
    ''');

#start boostrap
def boostrap(request):
    return render(request,'learn_boostrap.html');
# end boostrap 