from flask import Flask, request, render_template, redirect, abort
import requests
#import os

#os.environ['NO_PROXY'] = '127.0.0.1'

app = Flask(__name__)

url = 'https://to-do-list-api-ldkz.onrender.com/api/tasks'
#url = 'http://127.0.0.1:5000/api/tasks'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        tasks = requests.get(url).json()['tasks']
        completed = []
        incompleted = []

        #Dividir las tareas en grupos de completadas e incompletadas
        for task in tasks:
            if task['status'] == True:
                completed.append(task)
            else:
                incompleted.append(task)

        #Imrpimir las tareas completadas e incompletadas en consola
        print(f'COMPLETADAS: {completed}')
        print(f'INCOMPLETAS: {incompleted}')

        #Imprimir la lista de tareas en consola
        print(tasks)

        response = {'completed': completed,
                    'incompleted': incompleted,
                    'countCompleted': len(completed),
                    'countIncompleted': len(incompleted)
                    }
        return render_template('index.html', response=response)
    else:   #POST
        name = request.form['name']
        try:
            requests.post(url, json={"name":name})
            return redirect('/')
        except:
            return abort(500)

if __name__ == '__main__':
    app.run(debug=True)