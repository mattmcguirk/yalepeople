<?php
$conn = ldap_connect("directory.yale.edu") or die("Could not connect to yale directory");  
//#bind to the Yale LDAP server
$r = ldap_bind($conn) or die("Could not bind to yale directory");     
//#this holds the netID to be searched for
$netID = $_GET['netid'];
$result = ldap_search($conn,"ou=People,o=yale.edu", "(cn=".$netID.")") or die (ldap_error($conn));   // add a * wildcard if desired
//#get entry data as array
$info = ldap_get_entries($conn, $result);

//clean up the array we get from ldap_get_entries a little
//which returns both associative keys and numerical keys which contain
//the associative names (for some reason)

foreach($info as $index => $person)
{	

	//print_r($person);
	foreach($person as $k => $v)
	{
		if(!is_numeric($k))
		{
			$people[$index][$k] = $v[0];	 
		}
	}
}

	echo json_encode($people);
// #if using wild card search for multiple results:
//echo "Number of entries found: " . ldap_count_entries($conn, $result) . "<br />";
ldap_close($conn);

?>
