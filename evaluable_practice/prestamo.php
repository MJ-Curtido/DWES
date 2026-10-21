manu@manu:/var/www/tienda/t2$ cat prestamo.php 
<?php
$alias = "";
$email = "";
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$entryAlias = $_POST['alias'] ?? '';

	if (!is_string($entryAlias)) {
		$errors[] = 'Alias no es un texto.';
	} else {
		$alias = trim($entryAlias);

		if ($alias === ''){
			$errors[] = 'Escribe un alias';
		}
	}
}

$safeAlias = htmlspecialchars($alias, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
$safeEmail = htmlspecialchars($email, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
?>

<h1>Prestamo</h1>
<?php if (count($errors) > 0: ?>
<h2>Errores</h2>
<ul role="alert">
	<?php foreach($errors as $error): ?>
		<li><?= htmlspeacialchars($error, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></li>
</ul>
<?php endif; ?>

<form action="prestamo.php" method="post">
	<p>
		<label for="alias"> Alias</label>
		<input id="alias" name="alias" type="text" value="<?= $safeAlias ?>" required />
	</p>

        <p>
                <label for="email"> Email</label>
                <input id="email" name="email" type="email" value="<?= $safeEmail ?>" required />
        </p>


	<button type="submit"> Search</button>
</form>

