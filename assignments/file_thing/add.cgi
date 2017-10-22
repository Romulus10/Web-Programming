#!/usr/local/bin/php
<?php
    $text = $_GET['text'];
    $file = fopen('data.txt', 'a+');
    fwrite($file, $text);
    $data = fread($file, filesize($file));
    fclose($file);
    echo($data);
?>
