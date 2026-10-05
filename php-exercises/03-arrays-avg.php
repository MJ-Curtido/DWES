<?php
	$numbers = [];
	$sum = 0;

	for ($i = 0; $i < 10; $i++) { 
		$numbers[$i] = rand(1, 30);
	}

	for ($i = 0; $i < 10; $i++) {
		$sum += $numbers[$i];
		echo "Position " . $i .": " . $numbers[$i] . "<br>";
	}
	
	$avg = $sum / count($numbers);

	echo "<br><br>Average: " . $avg;
?>