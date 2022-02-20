<?php
require_once("includes/config.php");
require_once("includes/functions.php");
?>

<!doctype html>
<html>
<head>
  <title>My Blog</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <header></header>

  <?php

  $db = connect_db();

  if(isset($_GET['id']) && !is_null($_GET['id'])) {
    $q = $_GET['id'];
    $q = "select title, content from articles where id='$q'";
    fetch_article($db, $q);
  } else {
    echo("Welcome to my blog!");
  }

  ?>
</body>
</html>
