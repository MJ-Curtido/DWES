<?php
	$temps = [];
	
	for ($i = 0; $i < 10; $i++) {
		$temps[$i] = rand(1, 30);
	}

	$maxTemp = $temps[0];
	$minTemp = $temps[0];

	for ($i = 0; $i < 10; $i++) {
		echo "Temperature: " . $temps[$i] . "<br>";
		if ($temps[$i] > $maxTemp) $maxTemp = $temps[$i];
		if ($temps[$i] < $minTemp) $minTemp = $temps[$i];
	}

	$avg = array_sum($temps) / count($temps);

	echo "<br><br>Average: " . $avg;
	echo "<br>Max temperature: " . $maxTemp;
	echo "<br>Min temperature: " . $minTemp;
?>