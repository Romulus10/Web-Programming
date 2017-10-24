<?php
    $text = $_GET['text'];
    $file = fopen('data.txt', 'a+');
    fputs($file, $text);
    echo($text);
    fclose($file);
?>
