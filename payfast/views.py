from django.shortcuts import render
#from .models import payfast

def home(request):
    return render(request,'home.html')


def send_money(request):
   sender = request.form['sender']
   receiver = request.form['receiver']
   amount = int(request.form['amount'])

   if sender not in users or receiver not in users:
       return "Invalid sender or receiver"

       if user[sender]['balance']< amount:
           return "Insufficient funds"

           return redirect(url_for('home'))



