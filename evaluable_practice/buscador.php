manu@manu:/var/www/tienda/t2$ cat buscador.php 
<?php
# Posición 0: Nombre
# Posición 1: Categoría
# Posición 2: Días máx. de préstamo

$data = [
	['Portátil de aula', 'informática', 7],
	['Cámara réflex', 'fotografía', 5],
	['Micrófono inalámbrico', 'audio', 3],
	['Proyector portátil', 'informática', 2],
	['Tableta digital', 'informática', 5],
	['Trípode de cámara', 'fotografía', 4]
];
$search = "";
$error = "";
$results = [];

$entrySearch = $_GET['q'] ?? NULL;

if (!is_string($entrySearch)) {
	$error = 'Tipo no válido';
} else {
	$search = trim($entrySearch ?? '');

	if ($entrySearch !== NULL ) {
		if ($search === '') {
			$results = $data;
		} else {
			$orderA = array("á", "Á");
			$replaceA = "a";
			$searchA = str_replace($orderA, $replaceA, $search);

			$orderE = array("é", "É");
			$replaceE = "e";
			$searchE = str_replace($orderE, $replaceE, $searchA);

			$orderI = array("í", "Í");
			$replaceI = "i";
			$searchI = str_replace($orderI, $replaceI, $searchE);

			$orderO = array("ó", "Ó");
			$replaceO = "o";
			$searchO = str_replace($orderO, $replaceO, $searchI);

			$orderU = array("ú", "Ú");
			$replaceU = "u";
			$finalSearch = str_replace($orderU, $replaceU, $searchO);

			foreach ($data as $element) {
				if (strpos(strtolower($element[0]), strtolower($finalSearch))) {
					$results[] = $element;
				}
			}
		}
	}
}

$safeSearch = htmlspecialchars($search, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
?>

<h1>Buscador</h1>

<form action="buscador.php" method="get">
	<input id="searcher" name="q" type="text" value="<?= $safeSearch ?>" required />
	<button type="submit"> Search</button>
</form>

<?php if (count($results) > 0): ?>
<h2>Resultado:</h2>
<ul>
	<?php foreach ($results as $result): ?>
		<li>
			<?= htmlspecialchars($result[0], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?> - 
			<?= htmlspecialchars($result[1], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?> - 
			<?= htmlspecialchars($result[2], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?> - 
		</li>
	<?php endforeach; ?>
</ul>
<?php endif; ?>
<?php if ($_GET['q'] ?? NULL === NULL): ?>
	<p>Tipo no válido</p>
<?php endif; ?>

