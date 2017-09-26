<?php
/**
NAME:
Sean Batzel

Who did you help?

How?

Who helped you?

How?

**/
$data = file("Morse.txt");
echo "Verify Morse text\n"; // Added a newline to clarify output of the morse code mapping.

$translate = array();

foreach ($data as $k=>$v){
    $a = preg_split("/\t/", trim($v));
    echo "$a[0]: $a[1]\n";
    $translate[$a[0]] = $a[1];
}
$translate[' '] = ' ';
// Make the hash table with the keys being Morse Code and the values being the alphanumeric symbols.

echo "\n\n";

$Messages = file("MorseMessage.txt");
echo "List of messages\n\n";
foreach($Messages as $k=>$v){
    $message = "";
    echo "Message $k=$v";
    // Use the hashtable to translate the message
    foreach (explode('/', $v) as $x) {
        foreach ($translate as $key=>$value) {
            if ($x == $value) {
                $message = $message . $key;
            }
        }
    }
    echo "Translated $k=$message\n";
}
?>
