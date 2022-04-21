'use strict';

var utils = require('../utils/writer.js');
var Bd = require('../service/BdService');

const Ajv = require("ajv").default;
//use to get the schema
const schema = require('../models/schema.json');



//Get all buildings descriptions
module.exports.bdGET = function bdGET (req, res, next) {
  Bd.bdGET()
    .then(function (response) {
    	 utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

//delete a building description using its ID
module.exports.bdIdDELETE = function bdIdDELETE (req, res, next, id) {
  Bd.bdIdDELETE(id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
    
    var ret = JSON.parse(JSON.stringify(response));
      utils.writeJson(res, response, ret.code);
    });
};

//Get building description by Id
module.exports.bdIdGET = function bdIdGET (req, res, next, id) {
// Call the service related to that ...
  Bd.bdIdGET(id)
    .then(function (response) {
     
      	utils.writeJson(res, response);
      
    })
    .catch(function (response) {
    
    	var ret = JSON.parse(JSON.stringify(response));
  
        utils.writeJson(res, response, ret.code);
    });
};

//Create or update building description
module.exports.bdIdPUT = function bdIdPUT (req, res, next, body, id) {

  var value = req.body;
	var data = JSON.stringify(value);

	console.log(data);

	Bd.bdIdPUT(value, id)
	
	.then(function (response) {
		utils.writeJson(res, response);
		})
		.catch(function (response) {
		utils.writeJson(res, response);
		});
	
	/*
	//Validare Building Description
	var ajv = new Ajv({strict: false, validateFormats: false}); 
  	var validate = ajv.compile(schema);
  	var valid = validate(JSON.parse(data));
  	console.log(valid);
  	if (valid){ 
  	
   
		Td.tdIdPUT(value, id)

		.then(function (response) {
		utils.writeJson(res, response);
		})
		.catch(function (response) {
		utils.writeJson(res, response);
		});
		
	}
	else{
	
		utils.writeJson(res, validate.errors);
	
	}
	*/

};
