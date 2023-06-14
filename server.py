from flask import Flask, request, abort

# This flask app imitates an AWS Kenesis stream, or some web app that I've created that I want to integrate with another service. 
# For example, when I get a github message, I want my webapp to ding me. 
# This flask app sits and listens to the "/webhook" route much like my cool app would sit and listen to the "mycoolapp.com/github_webhook" route.
# Also like a kinesis stream would listen for it's route to be called from a data collection service. 

# Create the flask app
app = Flask(__name__)

# Define the webhook route
@app.route('/webhook',methods=['POST'])

def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'sucess',200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()

