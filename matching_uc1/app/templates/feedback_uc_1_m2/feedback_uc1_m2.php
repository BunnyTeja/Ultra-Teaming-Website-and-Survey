<?php

session_start([
    'cookie_lifetime' => 86400*7, // session expires in 7 days
]);

if (isset($_SERVER['HTTP_ORIGIN'])) {
    header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
    header('Access-Control-Allow-Credentials: true');
    header('Access-Control-Max-Age: 86400');    // cache for 1 day
}

// Access-Control headers are received during OPTIONS requests
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD'])) {
        header("Access-Control-Allow-Methods: GET, POST, OPTIONS");         
    }

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS'])) {
        header("Access-Control-Allow-Headers:{$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");
    }

    exit(0);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["submit"])) {
    // Check if form is submitted and submit button is clicked
    $rel_response = $_POST["rel_response"]; // Retrieve the selected value from the radio buttons
    // echo "Submitted value: " . $rel_response; // Print the submitted value
    $use_response = $_POST["use_response"]; // Retrieve the selected value from the radio buttons
    // echo "Submitted value: " . $use_response; // Print the submitted value
    $method = $_POST["method"];
    $use_case = $_POST["use_case"];
    $comments = $_POST["comments"];

    
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
    } else {
        $stmt = $conn->prepare("INSERT INTO relevant_responses (`rel_response`, `method`, `use_case`, `comments`) VALUES (?,?,?,?)");
        if (!$stmt) {
            die("Prepare failed: " . $conn->error);
        }
        $stmt->bind_param("ssss", $rel_response, $method, $use_case, $comments);
        $rel_response = $_POST["rel_response"]; 
        $stmt->execute();
         echo "Data inserted successfully";
        
        $stmt2 = $conn->prepare("INSERT INTO `useful_responses` (`use_response`, `method`, `use_case`, `comments`) VALUES (?,?,?,?)");

        // Bind the values you want to insert to the placeholders in the statement
        $stmt2->bind_param('ssss', $use_response, $method, $use_case, $comments);

        // Set the values to insert
        $use_response = $_POST["use_response"];

        // Execute the statement
        $stmt2->execute();
        header('Location: thankyou.html');
    }    
  
    $conn->close();
}
?>
