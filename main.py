import algorithms.bankers as bankers
import algorithms.fcfs as fcfs
import algorithms.priority as priority
import algorithms.roundRobin as rr
import algorithms.srtn as srtn
import algorithms.diningphilosophers as dinphil
import os
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import Response

app = Flask(__name__)

# Documentation Routes

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/docs/bankers', methods=['GET'])
def bankers_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/bankers.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_bankers(), name="bankers")

@app.route('/docs/dining-philosophers', methods=['GET'])
def dining_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/diningphilosophers.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_dining_philosophers(), name="dining-philosophers")

@app.route('/docs/fcfs', methods=['GET'])
def fcfs_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/fcfs.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_fcfs(), name="fcfs")

@app.route('/docs/priority', methods=['GET'])
def priority_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/priority.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_priority(), name="priority")

@app.route('/docs/roundrobin', methods=['GET'])
def rr_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/roundRobin.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_rr(), name="roundrobin")

@app.route('/docs/srtn', methods=['GET'])
def srtn_docs():
    working_dir = os.path.dirname(__file__)
    rel_path = "algorithms/srtn.py"
    abs_file_path = os.path.join(working_dir, rel_path)
    with open(abs_file_path, "r") as f:
        content = f.read()
    return render_template('docs/index.html', content=content, response=run_srtn(), name="srtn")

# REST routes

@app.route('/fcfs', methods=['GET'])
def run_fcfs():
    return fcfs.main()

@app.route('/priority', methods=['GET'])
def run_priority():
    return priority.main()

@app.route('/roundrobin', methods=['GET'])
def run_rr():
    return rr.main()

@app.route('/srtn', methods=['GET'])
def run_srtn():
    return srtn.main()
    
@app.route('/bankers', methods=['GET'])
def run_bankers():
    return bankers.main()    

@app.route('/dining-philosophers', methods=['GET'])
def run_dining_philosophers():
    return dinphil.main()    

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True)