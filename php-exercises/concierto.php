<?php
	require __DIR__ . '/funciones.php';

	$title = '<b>Concierto de prueba</b>';
	$ticketPrice = 18.5;
	$quantity = 3;
	$remainingCapacity = 1;
	$isStudent = False;

	$total = calculate_total($ticketPrice, $quantity);
	$totalDiscount = $total;

	if ($isStudent) {
		$totalDiscount = $total * 0.9;
	}

	$safeTitle = htmlspecialchars($title, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');

?>
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Ficha del concierto</title>
</head>
<body>
    <h1><?= $safeTitle ?></h1>
	<p><?='Ticket price: ' . number_format($ticketPrice, 2, ',', '.') . ' €'?></p>
	<p><?='Quantity: ' . $quantity?></p>
	<p><?='Total price: ' . number_format($total, 2, ',', '.') . ' €'?></p>
	<!-- He decidido, en el caso de que sea estudiante y tenga el descuento, mostrar por separado el descuento que tiene y cuánto sería el total contando con ese descuento -->
	<?php if ($isStudent): ?>
		<p>Discount: 10%</p>
		<p>Total price: <?=number_format($totalDiscount, 2, ',', '.') . ' €'?></p>
	<?php endif; ?>

	<p>
		<?php if ($quantity <= $remainingCapacity): ?>
			Remaining Capacity: <?= $remainingCapacity; ?>
		<?php else: ?>
			There is no capacity available
		<?php endif; ?>
	</p>
</body>
</html>