<?php
/**
NAME:
Sean Batzel

Version 1 2017-09-25:
    Initial solution.

Version 2 2017-09-26:
    Performance fix. The translation should now occur in O(n) time rather than O(n^2).

Who did you help?

How?

Who helped you?

How?

References:
https://stackoverflow.com/questions/11807796/add-space-after-every-4th-character
    Resolved issue with string concatenation.
http://php.net/manual/en/language.operators.comparison.php
    Verified string comparison operators.
https://stackoverflow.com/questions/1125730/how-can-i-split-a-comma-delimited-string-into-an-array-in-php
    Checked for a function to split a string on a delimiter.
http://php.net/manual/en/function.str-split.php
    Official documentation for the str_split function.
http://php.net/manual/en/function.explode.php
    Official documentation for the explode function.
http://php.net/manual/en/language.types.array.php
    Official array type documentation, checked to determine best way to use the type as an associative array.
**/
$data = file("Morse.txt");
echo "Verify Morse text\n"; // Added a newline to clarify output of the morse code mapping.

$translate = array();

foreach ($data as $k=>$v){
    $a = preg_split("/\t/", trim($v));
    echo "$a[0]: $a[1]\n";
    $translate[$a[1]] = $a[0]; // While printing the Morse code mappings, add to the $translate array
    // indexed by the Morse code letter.
}
$translate[' '] = ' '; // Make sure that the space character translates correctly.

// Make the hash table with the keys being Morse Code and the values being the alphanumeric symbols.

echo "\n\n";

$Messages = file("MorseMessage.txt");
echo "List of messages\n\n";
foreach($Messages as $k=>$v){
    $message = ""; // Initialize empty string to start the message.
    echo "Message $k=$v";
    // Use the hashtable to translate the message
    foreach (explode('/', $v) as $x) { // Break the string into an array delimited by '/'
        // Iterate through that array and add the correct alphabetic character.
        $message = $message . $translate[$x];
    }
    echo "Translated $k=$message\n";
}
?>
