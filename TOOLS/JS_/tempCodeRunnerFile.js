// ARGUMENTS
const addExpr = function (a, b) {
	console.log(arguments);
	return a + b;
};

addExpr(2, 5);
