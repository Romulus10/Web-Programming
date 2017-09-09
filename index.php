<DOCTYPE html>
<html>
    <head>
        <link rel='stylesheet' type='text/css' href='style.css'>
        <title>Home</title>
    </head>
    <body>
        <center><h3>Good morning, Dave.</h3></center>
        <div id='sidebar'>
        <p>
            <a href="https://github.com/Romulus10">Romulus10 on GitHub</a>
            <a href="https://www.python.org">Python Programming Language</a>
            <a href="https://ruby-lang.org">Ruby Programming Language</a>
            <a href="https://keybase.io/romulus10">Romulus10 on Keybase.io</a>
        </p>    
        <?php
            echo "Today's date."
            $date = date("d/m/Y");
            echo $date;
        ?>
        </div>
    </body>
</html>
