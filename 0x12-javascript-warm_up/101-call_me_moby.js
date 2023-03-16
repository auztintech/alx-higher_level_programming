#!/usr/bin/node

exports.myFunc = function (x, theFunction) {
	for (let i = 0; i < x; i++) {
		theFunction();
	}
};
