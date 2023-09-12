#!/usr/bin/node
function run (x, theFunction()){
	let i = 0;
	while(x > i){
		theFunction();
		i++;
	}
}
module.exports.run=callMeMoby;
