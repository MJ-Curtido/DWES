<?php
	$nombre = '';
	$modalidad = '';
	$plazasTexto = '';
	$plazas = null;
	$errores = [];
	$enviado = false;
	$modalidades = ['presencial', 'online'];

	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
		$nombreEntrada = $_POST['nombre'] ?? '';

		if (!is_string($nombreEntrada)) {
			$errores[] = 'El nombre debe llegar como texto.';
		} else {
			$nombre = trim($nombreEntrada);
			if ($nombre === '') {
				$errores[] = 'Escribe un nombre.';
			}
		}

		$modalidadEntrada = $_POST['modalidad'] ?? '';
		$plazasEntrada = $_POST['plazas'] ?? '';

		if (!is_string($modalidadEntrada)) {
			$errores[] = 'El formato de la modalidad no es válido.';
		} elseif (!in_array($modalidadEntrada, $modalidades, true)) {
			$errores[] = 'Selecciona una modalidad permitida.';
		} else {
			$modalidad = $modalidadEntrada;
		}

		if (!is_string($plazasEntrada)) {
			$errores[] = 'El formato de las plazas no es válido.';
		} else {
			$plazasTexto = trim($plazasEntrada);
			$plazas = filter_var($plazasTexto, FILTER_VALIDATE_INT);
			if ($plazas === false || $plazas < 1 || $plazas > 4) {
				$errores[] = 'Las plazas deben ser un entero entre 1 y 4.';
			}
		}

		$enviado = ($errores === []);
	}

	$nombreSeguro = htmlspecialchars($nombre, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
	$plazasSeguro = htmlspecialchars($plazasTexto, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
?>

<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Formulario inicial de inscripción</title>
</head>
<body>
    <h1>Inscripción a un taller</h1>
    <p>Este primer paso solo envía datos; todavía no los procesa.</p>

	<?php if ($errores !== []): ?>
		<h2>Revisa los datos</h2>
		<ul role="alert">
			<?php foreach ($errores as $error): ?>
				<li><?= htmlspecialchars($error, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></li>
			<?php endforeach; ?>
		</ul>
	<?php endif; ?>

    <form action="07-inscripcion-inicio.php" method="post">
        <p>
            <label for="nombre">Nombre ficticio</label>
            <input id="nombre" name="nombre" type="text" value="<?= $nombreSeguro ?>" required>
        </p>
        <p>
            <label for="modalidad">Modalidad</label>
            <select id="modalidad" name="modalidad" required>
                <option value="" <?= $modalidad === '' ? 'selected' : '' ?>>Elige una modalidad</option>
		<option value="presencial" <?= $modalidad === 'presencial' ? 'selected' : '' ?>>Presencial</option>
		<option value="online" <?= $modalidad === 'online' ? 'selected' : '' ?>>Online</option>
            </select>
        </p>
        <p>
            <label for="plazas">Número de plazas (1–4)</label>
            <input id="plazas" name="plazas" type="number" min="1" max="4" value="<?= $plazasSeguro ?>" required>
        </p>
        <button type="submit">Preparar inscripción</button>
    </form>

	<?php if ($enviado): ?>
		<h2>Resumen de la solicitud</h2>
		<p>Nombre: <?= $nombreSeguro ?></p>
		<p>Modalidad: <?= htmlspecialchars($modalidad, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></p>
		<p>Plazas: <?= $plazas ?></p>
	<?php endif; ?>
</body>
</html>
