import xlrd 				#To read Excel File
import csv					# importing csv module 
import numpy as np			#		#To generate Random Number 
from xlwt import Workbook	#To perforn Excel file I/O operation

temp = 0	#Variable
# create Workbook object from openpyxl
wb=Workbook()
# Give the location of the file 
loc = ("questions.xlsx") 
  
wb = xlrd.open_workbook(loc) 		#Opening Excel Workbook of Our Given Location
sheet = wb.sheet_by_index(0) 		#Select the Sheet Number(0,1,2....) 

#No. of Questions are = qnlenth
qnlenth=sheet.nrows	#Length of Sheet Questions

qnlist=[]	#Array of Questions
qnnumber=[]	#Array of Questions Number
optn1=[]	#Array of Option 1
optn2=[]	#Array of Option 2
optn3=[]	#Array of Option 3
optn4=[]	#Array of Option 4
optn5=[]	#Array of Option 5
trait=[]	#Array of Trait(Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Intellect )

#Reading ALL Values of from file in array formate:
for i in range (qnlenth):
	qnnumber=np.append(qnnumber,(sheet.cell_value(i, 0) ))
	qnlist=np.append(qnlist,(sheet.cell_value(i, 1) ))
	optn1=np.append(optn1,(sheet.cell_value(i, 2) ))
	optn2=np.append(optn2,(sheet.cell_value(i, 3) ))
	optn3=np.append(optn3,(sheet.cell_value(i, 4) ))
	optn4=np.append(optn4,(sheet.cell_value(i, 5) ))
	optn5=np.append(optn5,(sheet.cell_value(i, 6) ))
	trait=np.append(trait,(sheet.cell_value(i, 7) ))
 
# Extracting number of rows 
#print(sheet.nrows) 

from flask import Flask, redirect, url_for, request ,render_template
app = Flask(__name__) 

	
@app.route('/') 
def main(): 
	#return 'welcome to main page'
	
	return '<br><a href="http://127.0.0.1:5000/displayqn"><button onclick= "" align="center"  >Start Quiz</button></a>'
	
	
@app.route('/displayqn') 
def displayqn(): 	
	f = open("responce.csv", "w")
	f.truncate()
	f.close()
	
	"""
	if b is None:
		b = 0
	else:
		b = temp + 1
	print (b)
	"""
	b=0
	return render_template('quiz.html', qno = int(qnnumber[b]), qn = qnlist[b] ,op1 = optn1[b] , op2 = optn2[b], op3 = optn3[b],	op4 = optn4[b], op5 = optn5[b], trait = trait[b])	
	

@app.route('/next',methods = ['POST']) 
def next():
	
	if request.method == 'POST': 
		responceqno = request.form['qno']				#Question Number
		responceqno = int(responceqno)
		ans = float(request.form['q'])			#option selected/Value for question
		ans = int(ans)
		qtrait = request.form['trait']			#Trait for Question
	else:
		responceqno=0
		ans=0
		qtrait=0
	print (responceqno)
	print (ans)
	print (qtrait)
	
	with open("responce.csv", "a") as recordbook:
		writer = csv.writer(recordbook)
		writer.writerow([responceqno,ans,qtrait])
	
	if(responceqno == 50 ):		#50 is the number of questions
		return redirect(url_for('result'))
	else:
		b=responceqno
		return render_template('quiz.html', qno = int(qnnumber[b]), qn = qnlist[b] ,op1 = optn1[b] , op2 = optn2[b], op3 = optn3[b],	op4 = optn4[b], op5 = optn5[b], trait = trait[b])	
	#, trait = trait[b])	
	
	


@app.route('/result') 
def result():  
	return redirect(url_for('output')) 
	'''
	if request.method == 'POST': 
		q = request.form['q'] 
	else:  
		return redirect(url_for('main'))
	'''
@app.route('/output') 
def output():
	result_array=[]
	n=0
	a=0
	e=0
	c=0
	o=0
	with open("responce.csv", "r") as readresult:
		reader = csv.reader(readresult)
		for row in reader:
			print(row)
			result_array.append(row)
			
	result_array = [t for t in result_array if t]	#removing empty row for array
	temparray = []
	for num in result_array:	#removing duplicate row
		if num not in temparray:
			temparray.append(num)
	result_array = temparray
	#print(result_array)
		
	for data in result_array:
		#Extraversion
		if(data[2]=='Extraversion'):
			e=20	#default
			#1 11 21 31 41 question
			if( data[0]=='1' or data[0]=='11' or data[0]=='21' or data[0]=='31' or data[0]=='41'):
				e = e + int(data[1])
			#6 16 26 36 46
			else:
				e = e - int(data[1])
			
				
		#Agreeableness
		elif (data[2]=='Agreeableness'):
			a=14	#default
			#7 17 27 37 47 question
			if( data[0]=='7' or data[0]=='17' or data[0]=='27' or data[0]=='37' or data[0]=='47'):
				a = a + int(data[1])
			#2 12 22 32 42
			else:
				a = a - int(data[1])	

		#Conscientiousness
		elif (data[2]=='Conscientiousness'):
			c=14	#default
			#8 18 28 38 48 question
			if( data[0]=='8' or data[0]=='18' or data[0]=='28' or data[0]=='38' or data[0]=='48'):
				c = c + int(data[1])
			#3 13 23 33 43 
			else:
				c = c - int(data[1])
			
		#Emotional Stability /N
		elif (data[2]=='Emotional Stability'):
			n=38	#default
			#9 19 29 39 49 question
			if( data[0]=='9' or data[0]=='19' or data[0]=='29' or data[0]=='39' or data[0]=='49'):
				n = n + int(data[1])
			#4 14 24 34 44
			else:
				n = n - int(data[1])
		#Intellect/openness
		elif (data[2]=='Intellect'):
			o=8	#default
			#5 15 25 35 45 question
			if( data[0]=='8' or data[0]=='18' or data[0]=='28' or data[0]=='38' or data[0]=='48'):
				o = o + int(data[1])
			#10 20 30 40 50
			else:
				o = o - int(data[1])		
		else:
			print('else')
	print('\n\n\n\n\n')
	print ('Your Ocean Trait is:')
	print ('Openness',o)
	
	print ("Conscientiousness",c)

	print ('Extraversion',e)

	print ('Agreeableness ',a)

	print ('Neuroticism ',n)
	print('\n\n\n\n\n\n')
	
	return redirect(url_for('main'))

  	
if __name__ == '__main__': 
	app.run(debug = True) 
