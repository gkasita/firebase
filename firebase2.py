import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('sdk.json')
default_app = firebase_admin.initialize_app(cred, {'databaseURL': "https://connectingfirebasedbtopy-b04c9-default-rtdb.firebaseio.com"})

ref = db.reference('/')
ref.set({
    'Employee':
    {
        'emp1': {
            'name' : 'Parwiz',
            'lname' : 'Forogh',
            'age': 24
        },

        'emp2' : {
            'name' : 'Harry',
            'lname': 'Potter',
            'age': 25
        }
    }
})