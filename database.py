from flask import Flask, render_template, request, redirect
from forms import TextForm, CopyForm,DeleteForm,ReplaceForm,FindReplForm,AddForm
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'leo'
file_path = os.path.join('F:', 'example.txt') 

def define():
    copy_form=CopyForm()
    delete_form=DeleteForm()
    text_form=TextForm()
    replace_form=ReplaceForm()
    findreplace_form=FindReplForm()
    add_form=AddForm()
    return copy_form,delete_form,text_form,replace_form,findreplace_form,add_form

@app.route('/create', methods=['POST', 'GET'])
def createinformation():
    copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()
    if text_form.validate_on_submit():
        name = text_form.TextName.data            
        address = text_form.Path.data
        text = text_form.Text.data
        extension = text_form.Extension.data
        os.makedirs(address, exist_ok=True)
        Name = name + extension
        file_path = os.path.join(address, Name)
        with open(file_path, 'w') as file:
            file.write(text)
        return "Form was submitted successfully"
    return render_template('write.html',add_form=add_form, text_form=text_form, copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)

@app.route('/', methods=['POST', 'GET']) 
def HomePage():
    return render_template('home.html')

@app.route('/copy', methods=['POST', 'GET'])
def copytext():
   copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()
   if request.method == 'POST':
            text = request.form.get("Text")
            filename=request.form.get("TextName")
            ext=request.form.get("Extension")
            path=request.form.get("Path")
            
            with open(file_path, 'w') as file:
                file.write(text)
            text_form=TextForm()
            text_form.Text.data=text
            text_form.Path.data=path
            text_form.Extension.data=ext
            text_form.TextName.data=filename
            return render_template('write.html',add_form=add_form,text_form=text_form,copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)
   return "Something went wrong"

@app.route('/delete',methods=['POST','GET'])
def deltext():   
    copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()

    if request.method=='POST':
        text_form.TextName.data=request.form.get("TextName")
        text_form.Extension.data=request.form.get("Extension")
        text_form.Path.data=request.form.get("Path")
        return render_template('write.html',add_form=add_form,text_form=text_form,copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)
    return "Something went wrong"

@app.route('/replace',methods=['POST','GET'])
def reptext():
    copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()
    if request.method=='POST':
        text=''
        text_form.TextName.data=request.form.get("TextName")
        text_form.Extension.data=request.form.get("Extension")
        text_form.Path.data=request.form.get("Path")
        with open(file_path,'r') as file:
            text=text+file.read()
        text_form.Text.data=text
        return render_template('write.html',add_form=add_form,text_form=text_form,copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)

@app.route('/findreplace',methods=['POST','GET'])
def frtext():
    copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()

    if request.method=='POST':
        text=request.form.get("Text")
        find=request.form.get("FirstElement")
        replace=request.form.get("SecondElement")
        l=text.replace(find,replace)
        text_form.Text.data=l
        findreplace_form.FirstElement.data=''
        findreplace_form.SecondElement.data=''
        return render_template('write.html',add_form=add_form,text_form=text_form,copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)
    
@app.route('/cpfile',methods=['POST','GET'])
def cpfile():
    copy_form,delete_form,text_form,replace_form,findreplace_form,add_form=define()
    if request.method=='POST':
        text=request.form.get("Text") or ''
        choice=request.form.get("Choice")
        path=request.form.get("Path")
        if os.path.exists(path):
            file=''
            with open(path,'r') as f:
                file=file+f.read()
            text= file+text if choice=="Start" else text+file
            text_form.Text.data=text
            add_form.Path.data=''
            add_form.Choice.data=''
            return render_template('write.html',add_form=add_form,text_form=text_form,copy_form=copy_form,delete_form=delete_form,replace_form=replace_form,findreplace_form=findreplace_form)
        else:
            return "NO SUCH PATH"
    else:
        return "DID't RECEIVE POST"

@app.route('/shutdown',methods=['POST','GET'])
def sd():
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
     app.run(debug=True)
