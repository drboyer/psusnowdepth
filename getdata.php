<?php
// Gets the last 30 days of snowfall entries from the database and outputs it as JSON

error_reporting(E_ALL);
ini_set('display_errors', 1);

$depths = array();
$timestamps = array();
$results = array();


// Connect to database
try {
  $DBH = new PDO("mysql:host=localhost;dbname=DB_NAME", "USERNAME", "PASSWORD");
  $DBH->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
  die("Could not connect to database.");
}

try {
	$query = "SELECT date, depth FROM snowdepth ORDER BY date DESC LIMIT 30";
	$STH = $DBH->query($query);

	$i = 0;
	while($row = $STH->fetch()) {
		$dateObj = new DateTime($row['date']);
		$JSTimestamp = $dateObj->getTimestamp() * 1000;
		//$timestamps[] = $JSTimestamp;
		//$depths[] = intval($row['depth']);
		$results[] = array($JSTimestamp, intval($row['depth']));

		$i++;
	}

	$results = array_reverse($results);

	/*$depths = array_reverse($depths);      // Flip the order to display in the graph correctly

	for ($i=0; $i < sizeof($depths); $i++) { 
		$results[$i] = array($timestamps[$i], $depths[$i]);
	}
	*/

	echo json_encode($results);
} catch (PDOException $e) {
  die("Error fetching data from database.");
}

?>
