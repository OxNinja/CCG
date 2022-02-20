<?php

function connect_db(){
  $db = new mysqli(Config::$db_host, Config::$db_user, Config::$db_pass, Config::$db_db);
  if($db->connect_error){
    die($db->connect_error);
  }
  return $db;
}

function fetch_article($db, $q){
  $r = $db->query($q);
  $db->close();

  if($r->num_rows > 0){
    $r = $r->fetch_row();
    echo("<article><h1>$r[0]</h1><p>$r[1]</p></article>");
  } else {
    echo("Article not found.");
  }
}


?>
