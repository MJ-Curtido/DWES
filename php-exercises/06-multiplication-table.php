<?php
	function multiplicationTable($number) {
		for ($i = 1; $i <= 10; $i++) {
			echo $number . " x " . $i . " = " . ($number * $i) . "<br>";
		}
	}

	multiplicationTable(7);
?>