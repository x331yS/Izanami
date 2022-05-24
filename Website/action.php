<?php



$color = $_POST['color'];
list($r, $g, $b) = sscanf($color, "#%02x%02x%02x");


include '../../../config.php';
$conn = new mysqli("$servername", "$username", "$password", "$dbname");
echo $dbname;
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "UPDATE currentprofile SET profile = 'WEBSITE', red=$r, green=$g, blue=$b";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

header("Location: /");
?>
