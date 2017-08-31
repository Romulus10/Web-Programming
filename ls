#!/opt/lampp/bin/php
<?php

if ($argc == 1) {
    $dir = opendir('./');
} else {
    $dir = opendir($argv[1]);
}

while($list[] = readdir($dir));
closedir($dir);
array_pop($list);

foreach ($list as $k=>$v) {
    echo "$k: $v\n";
}

?>
