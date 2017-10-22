#!/usr/local/bin/php
<?php
    $text = $_GET['text'];
    $file = fopen('data.txt', 'a+');
    fwrite($file, $text);
    fseek($file, 0);
    $data = fread($file, filesize('data.txt'));
    echo($data);
    fclose($file);
?>
