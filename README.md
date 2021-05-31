# ProtoSem OS Assignment

This is an assignment submission that implements a simple RESTful API that demonstrates process scheduling algorithms (with pre-filled sample data) and runs them on docker and deploys to kubernetes.

## Getting Started

### Running the app locally

To run the app, simply clone the repo and run `pip install requirements.txt` and then run `python main.py`

### Building and running on docker

This project includes a dockerfile to build and run your project on docker.

1. Clone the repo and build the container using ```docker build . -t protosem-os-assignment:latest```
2. Run the container using ```docker run -d -p 5001:5001 protosem-os-assignment```
3. Open [localhost port 5001](http://localhost:5001)! (we assume you're running locally)

## File Structure

This is a very small app that really doesn't need a file structure documentation. It's pretty obvious.
But for the sake of it, the important things to know are that: 

1. Algorithm implementations are included in the `/algorithms` folder
2. Proof of execution (screens) is included in the `/screenshots` folder

