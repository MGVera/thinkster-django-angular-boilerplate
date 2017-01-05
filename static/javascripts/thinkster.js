(function(){
	'use-strict';

	angular
		.module('thinkster', [
			'thinkster.routes',
			'thinkster.config',
			'thinkster.authentication'
			]);

	angular
		.module('thinkster.routes', ['ngRoute']);

	angular
		.module('thinkster.config', []);

	angular
		.module('thinkster')
		.run(run);

	run.$inject = ['$http'];

	function run($http){
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

	//Header expected by Django
    $http.defaults.xsrfCookieName = 'csrftoken'; 

}

 
})();



