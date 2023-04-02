import os
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import pandas as pd


def index(request):
    context={}
    
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        if uploaded_file.name.endswith('.csv'):
            # save the file in media folder
            savefile = FileSystemStorage()
            
            name = savefile.save(uploaded_file.name, uploaded_file)
            
            file_directory = os.path.join(os.getcwd(), 'media', name)
            print(file_directory)
            # do something with the uploaded CSV file here
            readfile(file_directory)
            return redirect(results)
        else:
            messages.warning(request, 'opps try CSV please')
            
    return render(request, 'index.html')


def readfile(filename):
    my_file = pd.read_csv(filename, sep='[:;,|_]', engine='python')
    
    data = pd.DataFrame(data=my_file, index=None)


def results(request):
    
    return render(request, 'results.html')

