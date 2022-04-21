'use strict';

var BD = require('../models/bd');

var utils = require('../utils/BDserialize.js');

/**
 * Retrieves the list of Building Descriptions
 *
 * no response value expected for this operation
 **/
exports.bdGET = function() {
  return new Promise(function(resolve, reject) {
    // find a BD based on the Id; 
      BD.find({},{_id:0, __v:0}, function (err, docs) {
      	 if (err){ 
        	console.log(err) 
    	}

    	if(docs === null){
    		reject({
		  "code": 404,
		  "message": "Not found"
		});	
    	}else{
    		resolve(docs);	

    	}
    	
  	
	});
  });
}


/**
 * Deletes the Building Description
 *
 * id String id of the Building Description
 * no response value expected for this operation
 **/
exports.bdIdDELETE = function(id) {
  return new Promise(function(resolve, reject) {
	
	  BD.findOneAndDelete({id: id}, {_id:0, __v:0}, function (err, docs) {
      	 if (err){ 
        	console.log(err) 
    	}
	console.log(docs);
    	if(docs === null){
    		reject({
		  "code": 404,
		  "message": "Not found"
		});	
    	}else{
    		//remove the triple; 
   	utils.removeBD(id);
        		resolve();	
    	} 	
	});	   
 });
}


/**
 * Retrieves a Building Description
 *
 * id String id of the Building Description
 * returns Object
 **/
exports.bdIdGET = function(id) {
  return new Promise(function(resolve, reject) {
 // console.log(id);
 
      // find a BD based on the Id; 
      BD.findOne({id: id}, {_id:0, __v:0}, function (err, docs) {
      	 if (err){ 
        	console.log(err) 
    	}

    	if(docs === null){
    		reject({
		  "code": 404,
		  "message": "Not found"
		});	
    	}else{
    		resolve(docs);	

    	}
    	
  	
	});

  });
}


/**
 * Creates a new Building Description, or updates an existing one
 *
 * body Object The Building Description object
 * id String id of the Building Description
 * no response value expected for this operation
 **/
exports.bdIdPUT = function(body,id) {
       
  return new Promise(function(resolve, reject) {
  
 var condition = {'id':id};
 var doc = body;
 BD.findOneAndUpdate(condition,doc,{upsert:true},function(err,doc){
    if (err){
    	console.log(err);
    	reject();
   }else{
    
   	//remove the triple in case of update; 
   	utils.removeBD(id);
   	
   	//serialize
   	utils.storeBD(JSON.stringify(body));
    
   	resolve();
   }
 });

  });
}

