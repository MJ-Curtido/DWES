<?php
	require_once '06-multiplication-table.php'

	function showTablesBetween($start, $end) {
		for ($i = $start; $i <= $end; $i++) {
			multiplicationTable($i);
			echo "<br><br>";
		}
	}

	showTablesBetween(1, 7);
?>