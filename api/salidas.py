
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Departures - Salidas</title>
  <link rel="stylesheet" href="../css/jquery-1.11.1.min.js">
  <style>
    body {
      margin: 0;
      background-color: #111;
      font-family: 'Courier New', Courier, monospace;
      color: #f1c40f;
    }
    header {
      background: #000;
      padding: 10px;
      text-align: center;
      font-size: 2rem;
      font-weight: bold;
      color: #f1c40f;
      letter-spacing: 2px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    th, td {
      padding: 12px;
      text-align: center;
      border-bottom: 1px solid #333;
    }
    th {
      background-color: #222;
      color: #f1c40f;
      font-size: 1.1rem;
    }
    td {
      color: #ecf0f1;
      font-size: 1.3rem;
    }
    tr:nth-child(even) {
      background-color: #1c1c1c;
    }
    tr:hover {
      background-color: #333;
    }
  </style>
</head>
<body>
  <header>✈️ DEPARTURES - SALIDAS</header>
  <table id="tabla-vuelos">
    <thead>
      <tr>
        <th>Hora</th>
        <th>Destino</th>
        <th>Vuelo</th>
        <th>Puerta</th>
        <th>Embarque</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

  <script>
    async function cargarVuelos() {
      try {
        const respuesta = await fetch("https://api-vuelos.vercel.app/salidas");
        const datos = await respuesta.json();
        const cuerpo = document.querySelector("#tabla-vuelos tbody");
        cuerpo.innerHTML = "";

        datos.forEach(vuelo => {
          const fila = document.createElement("tr");
          fila.innerHTML = `
            <td>${vuelo.hora}</td>
            <td>${vuelo.destino}</td>
            <td>${vuelo.vuelo}</td>
            <td>${vuelo.puerta}</td>
            <td>${vuelo.estado}</td>
          `;
          cuerpo.appendChild(fila);
        });
      } catch (error) {
        console.error("Error al cargar los datos:", error);
      }
    }

    cargarVuelos();
    setInterval(cargarVuelos, 60000);
  </script>
</body>
</html>
