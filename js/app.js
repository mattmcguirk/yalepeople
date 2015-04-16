angular.module('yalePeople', [])
	.controller('SearchController', ['$scope', '$http', function($scope, $http) {

	$scope.search = function ()
	{
		if($scope.name)
		{
			queryString = 'ext/ldap.php?netid=' + "*" + $scope.name + "*";
		}
		$http.get(queryString).success(function(result){
	    	$scope.people = result;
		});

	}
}]);
