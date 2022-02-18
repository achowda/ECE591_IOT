# ECE591_IOT
Spring 2022 IOT Assignments NCSU

## Description
Implements a HTTP client in python that can connect with a HTTP server to transfer data. 

Code highlights
- Python requests module was used to implement the HTTP client
- Python time module was used to benchmark the file transfer time
- Python statistics module was used to average the time and calculate standard deviation

## Software Requirements
- `pip install python`
  - Requires python 3.7.4 or later
- `pip install requests`
  - Abstracted HTTP library that can be used to request and decode data from a HTTP server 
- HTTP module comes pre-installed with python 3.7.4 or later

### Setup used for experiment
![image](https://user-images.githubusercontent.com/99939969/154616582-9a70b923-41bf-4a98-a7fe-8372ac5fd988.png)


### Deploying the server
A HTTP server was deployed on Port 8081 from the above location using the python cmd, “python –m http.server 8081”

![image](https://user-images.githubusercontent.com/99939969/154616363-27a3895f-6c64-48d0-932e-ceaf600432e7.png)


### HTTP Transfer Time Recorded

![image](https://user-images.githubusercontent.com/99939969/154616760-5c1a0d3f-1091-44c1-a76e-aee5d7f9104f.png)


