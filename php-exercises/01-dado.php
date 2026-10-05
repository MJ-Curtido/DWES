<?php
	$dice = rand(1, 6);

	if ($dice == 1) {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Dice-1-b.svg';
	} else if ($dice == 2) {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Dice-2-b.svg';
	} else if ($dice == 3) {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Dice-3-b.svg';
	} else if ($dice == 4) {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Dice-4-b.svg';
	} else if ($dice == 5) {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/0/08/Dice-5-b.svg';
	} else {
		$image = 'https://upload.wikimedia.org/wikipedia/commons/2/26/Dice-6-b.svg';
	}

	echo 'Result: ' . $dice . '<br><br>';
	echo '<img src = "' . $image . '" width="150" alt="dice">';
?>