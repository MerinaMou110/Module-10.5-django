from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d= {'author':'Rahim','age':15,'lst':['python','is','best'],'str':'Python Is Fun','str1':'Today is very good day',
        'lst1': "First \nSecond \nThird ", 'my_date_time': datetime.datetime(2022, 12, 1, 9, 0),
        'num_tomato':2, 'slash':"I'will go", 'value':"",
        'today' : datetime.datetime.now(),'val':'' ,'sum':100,
        'title' : '<script>alert("XSS attack!");</script>' ,
        'text':2345671, 'var':['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],'courses':[
        {
            'id':1,
            'name': 'python',
            'fee': 5000

        },
        {
            'id':2,
            'name': 'django',
             'fee': 10000

        },
        {
            'id':3,
            'name': 'C',
             'fee': 1000

        },
    
    ]}
    return render(request,'index.html',d)
