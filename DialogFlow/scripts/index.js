// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
// To be used in the inline editor after enabling fulfillment.
'use strict';
 
const axios = require('axios');
const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');
 
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
  var queryResult = request.body.queryResult;
 
  function welcome(agent) {
    agent.add(`Welcome to my agent!`);
  }
  
  function fallback(agent) {
    agent.add(`I didn't understand`);
    agent.add(`I'm sorry, can you try again?`);
  }
 function general_search_handler(agent)
  {
    const query = queryResult.queryText;
	const word = agent.parameters.appliances;
    agent.add(`Here are 2 relevant products.`);
    var query1= query + "+" + word;
	var res = query1.split(' ').join('+');
    var count = 1;
    return axios.get(`http://lowescampushackathon.pythonanywhere.com/general_search/${res}`)
      .then((result) =>{
      result.data.map(wordObj =>{
              	agent.add(`Details of Product `+ count);
        	count+=1;
        	agent.add(`Rating: ` + wordObj.ratings);
        	agent.add(`Web Link: ` + wordObj.website_link);
        	agent.add(`Price: `+ wordObj.now_price);
      });
    });
 }
  
  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  intentMap.set('show_product_details', general_search_handler);
  // intentMap.set('your intent name here', googleAssistantHandler);
  agent.handleRequest(intentMap);
});
