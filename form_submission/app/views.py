from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect
from .producer import producer

from kafka.admin import KafkaAdminClient, NewTopic
from .utils import get_db_handle

db, db_col = get_db_handle('admin','user')


# admin_client = KafkaAdminClient(
#     bootstrap_servers="localhost:9092", 
#     client_id='test'
# )

def home(request):
    return HttpResponseRedirect('/signup/')

def thanks(request):
    return render(request, 'app/thanks.html')

def login(request):
		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			user = {
				'email':email,
				'password':password
			}
			doc = db_col.find(user)
			return render()
			# if db_col.find(user):
			# 	print('found')
		return render(request, 'app/login.html')

def signup(request):
		if request.method == 'POST':
			email = request.POST['email']
			if request.POST['password'] == request.POST['repeatPassword']:
				password = request.POST['password']
				db_object = {
					'email':email,
					'password':password
				}
				db_col.insert_one(db_object)
		return render(request, 'app/signup.html')

def index(request):

	form = UserForm()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			data = {'message' : request.POST['message']}
    		# producer.send('numtest', value=data)
			# return HttpResponseRedirect('/thanks/')
			
	context = {'form':form}
	return render(request, 'app/index.html', context)