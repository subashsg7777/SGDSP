<html>
<body>

<form method=”post” action=”<?php echo $_SERVER[‘PHP_SELF’];?>”>
Name: <input type=”text” name=”username”>
<input type=”submit” name=”save” value=”submit”>
</form>


<?php
if ($_SERVER[“REQUEST_METHOD”] == “POST”) {
// collect value of input field
$username = $_REQUEST[‘username’];
if (empty($username)) {
echo “Username is empty”;
} else {
echo $username;
}
}
?>
</body>
</html>