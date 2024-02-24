__Objective__
- Prove the ability to rate limit requests per minute to no more than 5 requests / minute
  
__Pre-requisities__

1. Sign up for Kong Konnect [here](https://cloud.konghq.com/register)
2. Go through the Konnect [Get Started](https://docs.konghq.com/konnect/getting-started/)
3. Setup rate limiting plug-in to limit the number of requests to the service to 5 requests per minute
4. Run the ```pip3 install -r requirements.txt``` to install dependencies
5. Go to Kong Konnect plugins page
6. Search and select 'Rate Limiting'
7. Enable the plugin
8. Select Scoped and add the following configurations <br/>
  a. Gateway Service: 'example_gateway_service - xxxx' <br/>
  b. Route: 'httpbin - xxxx' <br/>
  c. Error Code: 429 <br/>
  d. Error Message: 'API rate limit exceeded. Please try again in 1 min.' <br/>
  e. Minute: 5 

__Demo Flow__
1. Run the demo.py first to simulate when API requests > 5 per minute <br/>
  a. Show on the console that last request (6th request) is a 429 status code with custom error message
2. Run the command `locust`
3. Navigate to http://localhost:8089
4. Setup a load test of: <br/>
  a. Num of users: 10 <br/>
  b. Ramp up: 10
5. Watch the number of errors increase as requests per second increase

__Measurement__
1. Navigate to the statistics dashboard
2. Show the number of success vs num of errors is a difference of 5 - highlighting that the rate limiting plugin is working
