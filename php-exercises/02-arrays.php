<?php
	$numbers = [];

	for ($i = 0; $i < 10; $i++) { 
		$numbers[$i] = rand(1, 30);
	}

	for ($i = 0; $i < 10; $i++) {
		echo "Position " . $i .": " . $numbers[$i] . "<br>";
	}
?>