__Pre-requisities__

1. Sign up for Kong Konnect [here](https://cloud.konghq.com/register)
2. Go through the Konnect [Get Started](https://docs.konghq.com/konnect/getting-started/)
3. Setup rate limiting plug-in to limit the number of requests to the service to 5 requests per minute
4. Run the ```pip3 install -r requirements.txt``` to install dependencies 

__Demo Flow__
1. Run the demo.py first to simulate when API requests > 5 per minute
  a. Show on the console that last request is 429 status code with custom error message
2. Run the command `locust`
3. Navigate to http://localhost:8089
4. Setup a load test of: <br/>
  a. 10 users <br/>
  b. ramp up of 10
5. Watch the number of errors increase 
