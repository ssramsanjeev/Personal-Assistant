from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,ValidationError,TextAreaField,SelectField,RadioField
from wtforms.validators import DataRequired,Length

class TextForm(FlaskForm):
    textName=StringField("File Name",validators=[DataRequired(),Length(min=5)])
    path=StringField("Path",validators=[DataRequired(),Length(min=3)])
    Extension=SelectField("Extension",choices=[('.txt','.txt'),('.py','.py'),('.c','.c'),('.java','.java')])
    Text=TextAreaField("Text")
    submit=SubmitField("Submit")

class CopyForm(FlaskForm):
    Text=TextAreaField("Text")
    Path=StringField("Filepath :")
    Extension=SelectField("File type : ",choices=[('.txt','text file'),('.py','python'),('.c','c'),('.java','java')])
    TextName=StringField("File Name : ")

class DeleteForm(FlaskForm):
    Path=StringField("Filepath :")
    Extension=SelectField("File type : ",choices=[('.txt','text file'),('.py','python'),('.c','c'),('.java','java')])
    TextName=StringField("File Name : ")

class ReplaceForm(FlaskForm):
    Path=StringField("Filepath :")
    Extension=SelectField("File type : ",choices=[('.txt','text file'),('.py','python'),('.c','c'),('.java','java')])
    TextName=StringField("File Name : ")

class FindReplForm(FlaskForm):
    FirstElement=StringField("Element To Be Replaced",validators=[DataRequired()])
    SecondElement=StringField("Element To Replace")
    Text=TextAreaField("Text",validators=[DataRequired()])
    save=SubmitField("Replace All")

class AddForm(FlaskForm):
    Path=StringField("File path",validators=[DataRequired(Length(min=3))])
    Choice=RadioField('Select an Option',choices=[('Start','Start'),('End','End')],validators=[DataRequired()])
    save=SubmitField("Copy Text")
    Text=TextAreaField("Text")

