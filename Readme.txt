<!DOCTYPE html>
<html>
<head>
	<title>QUESTIONS!</title>
</head>
<body>

<form action="queryconnect.php" method="POST">
<input type="text" name="ques" placeholder="drop your questions here">
<br><br>
<button type="submit" >SUBMIT</button>

</form>


<form action="querypage.php" method="POST">
<br><br>
Click here to view previously asked questions randomly.
<br><br>
<button onclick="$check_row">CHECK!</button>	
<br><br>
</form>


<?php
session_start();

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "uhere";

//create connection to the database

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error){
	die ("connection failed!" . $conn->connect_error);
}else {
	//echo "connected successfully! <br />";
};


$display = "SELECT * FROM querytable ORDER BY RAND() LIMIT 2" ;

$check = $conn->query($display);
$check_row = $check->fetch_array();

$_SESSION['id']= $check_row['queryID'];

$_SESSION['name'] = $check_row['queryname'];

$ins = $_SESSION['id'];
$thequery = $_SESSION['name'];



while ($check_row = $check->fetch_array()) {
	echo  $thequery . "<br><br />";

}
?>

<form action="queryans.php" method="POST">
<i>Give your answers here! </i><br>
<input type='text' name='Ans' style="height: 100px; width: 200px">
<br>
<button type="submit" >SUBMIT</button>
</form>

</body>
</html>
