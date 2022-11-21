# freeday_bot

This is the GitHub repository related to the Freeday case. This is Francesco's work. 

First of all, I granted access to the implemented Dialogflow CX agent to k.ramsodit@freeday.ai. 


LEGENDA:
main.py // this file is my try of cloud function for dialogflow CX. I connected the webhook to the agent, creating a cloud function. I tried to implement a rest api using fastapi but I still seem to get specific errors, being unable to retrieve the dialogflow request json file and push it back to the agent. 

static_api.py // this file is the static version of the weather api call, given a date and a location. The script checks for validity, calls the external link, scrapes the data it needs and outputs it to the terminal. 

SOLUTION DESIGN:
I think the main issue here was the fact that I had to learn both dialogflow cx and web frameworks from stratch, ending up dealing with things that were not exaclty what I do everyday. In order to finalize it, I would need to spend some more time in understanding web frameworks (Fastapi or Django seem to be the most used ones) and how to exactly connect them to webhooks: I am confident that I could do that relatively fast. Once the script (main.py) for the web framework is correctly specified and deployed on gcp, everything should be set to work. In fact, the webhook in the agent is already pointing to the cloud function right now.

This being said, I loved working on this bot! I liked very much the idea behind designing the different interactions, parameters and intents. Also, I feel thrilled and eager to do even better in the future, learning web frameworks and their implementations even more. 

I cannot wait for your final answer. Hear from you then!

Best,
Francesco Mattera





