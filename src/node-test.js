

// Basic Node.js test file
var http = require('http');
var url = require('url');

// Create server to receive and respond to requests
http.createServer(function(request, response) {

	process.stdout.write("Recieved request\n");

	// Get the url parameters
	var _get = url.parse(request.url, true).query;

	response.writeHead(200, {
		'Content-Type': 'text/plain'
	});
	response.end("Hello World! Echo=" + _get['echo']);

}).listen(8080);

