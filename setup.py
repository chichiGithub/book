"""This module will generate a mini webserver"""

from bookapp import app



#config is a dictionary in the Flask class
if __name__=='__main__':
    app.run(debug=True,port=8082)