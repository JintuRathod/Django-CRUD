from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from Home.models import Entry

# Create your views here.


#dynamically pass url in browser-url 3-type int, str, slug
def slug(request, sg):
    return HttpResponse(sg)


def home(request):
    return render(request, 'Home.html')


def show(request):
    data  = Entry.objects.all()
    return render(request, 'show.html',{'Data': data})


def send(request):
    if request.method == 'POST':
        ID = request.POST.get('id') # this and below both are working to fetch data from html file
        Data1 = request.POST['data1'] # this and above both are working to fetch data from html file
        Data2 = request.POST['data2']
        Entry(ID=ID, Data1=Data1, Data2=Data2).save()  # assigning html data to database column   and save it 
        
        return render(request, 'Home.html',{'msg':'Data Inserted Successfully'})  # just rendering with dictionary
    else:
        return HttpResponse("404 - Not Fount ")


def delete(request):
    ID = request.GET['id'] # fetch id from url with get request
    Entry.objects.filter(ID = ID).delete()  # filter database table and assign fetched id. and perform delete function
    return HttpResponseRedirect('/show/')   # redirecting to (project/show/)url


#for edit get an id and filter it to DB Table ID and assign table column data to python variable
def edit(request):
    ID = request.GET['id']
    data1 = data2 ="Not Available"  # if id not present then shows than in columns
    for data in Entry.objects.filter(ID = ID):  # assign id to table ID column with filter and pass to loop variable(data) 
        data1 = data.Data1 # simply meaning that (data1 = ID.Data1) assign table values to python variables
        data2 = data.Data2
        return render(request,'edit.html', {'ID': ID, 'data1':data1, 'data2':data2})  #return render with dictionary


# insert edited data into database table 
def recordedited(request):
    if request.method == 'POST': # check for form method type
        ID = request.POST['id'] # fetch data 
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry(ID = ID, Data1 = data1, Data2 = data2).save() # assign data to DB table and save it..
        return HttpResponseRedirect('/show/', {'msg': 'Edited Successfully...'})   # redirecting to specific page required