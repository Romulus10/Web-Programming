<?php

if ($argc == 1) {
    $dir = opendir('./');
} else {
    $dir = opendir($argv[1]);
}

while($list[] = readdir($dir));
closedir($dir);
array_pop($list);

foreach ($list as $v) {
    if (is_dir($v)) {
        $string = "d $v\n";
    } else {
        $string = "f $v\n";
    }
    echo $string;
}

?>
