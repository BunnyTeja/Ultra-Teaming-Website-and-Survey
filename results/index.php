<?php
// Connect to the database
$servername = "localhost";
$username = "admin";
$password = "aiadmin";
$db_name = "Feedback-Receiver";
// Create connection 
$conn = new mysqli($servername, $username, $password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve data for relevant responses
$sql = "SELECT rel_response, COUNT(*) AS count FROM relevant_responses GROUP BY rel_response";
$result = $conn->query($sql);
$rel_labels = array();
$rel_data = array();
while($row = $result->fetch_assoc()) {
    $rel_labels[] = $row['rel_response'];
    $rel_data[] = $row['count'];
}

// Retrieve data for useful responses
$sql = "SELECT use_response, COUNT(*) AS count FROM useful_responses GROUP BY use_response";
$result = $conn->query($sql);
$use_labels = array();
$use_data = array();
while($row = $result->fetch_assoc()) {
    $use_labels[] = $row['use_response'];
    $use_data[] = $row['count'];
}

$conn->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Feedback Results</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>

<div style="width: 40%; float: left;">
        <canvas id="relChart"></canvas>
        <div style="text-align:center;font-weight:bold;text-decoration:underline">Pie Chart for Relevant Responses</div>
    </div>
    <div style="width: 40%; float: left;">
        <canvas id="useChart"></canvas>
        <div style="text-align:center;font-weight:bold;text-decoration:underline">Pie Chart for Useful Responses</div>
    </div>
    <script>
        // Create pie chart for relevant responses
var relChart = new Chart(document.getElementById('relChart'), {
    type: 'pie',
    data: {
        labels: <?php echo json_encode($rel_labels); ?>,
        datasets: [{
            data: <?php echo json_encode($rel_data); ?>,
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(153, 102, 255)',
            ]
        }]
    },
    options: {
    title: {
        display: true,
        text: 'Relevant Responses',
        fontSize: 14 // adjust font size as needed
    },
    legend: {
        labels: {
            fontSize: 12 // adjust font size as needed
        }
    }
}

});

// Create pie chart for useful responses
var useChart = new Chart(document.getElementById('useChart'), {
    type: 'pie',
    data: {
        labels: <?php echo json_encode($use_labels); ?>,
        datasets: [{
            data: <?php echo json_encode($use_data); ?>,
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(153, 102, 255)',
            ]
        }]
    },
    options: {
    title: {
        display: true,
        text: 'Useful Responses',
        fontSize: 14 // adjust font size as needed
    },
    legend: {
        labels: {
            fontSize: 12 // adjust font size as needed
        }
    }
}

});    
    </script>
</body>
</html>
