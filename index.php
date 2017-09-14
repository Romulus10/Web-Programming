<!DOCTYPE html>
<html>
    <head>
        <link rel='stylesheet' type='text/css' href='style.css'>
        <title>Home</title>
    </head>
    <body>
        <div id='xkcd'>
            <a href='https://www.xkcd.com/'>
            <img src='pointers.png' alt='XKCD'>
            </a>
        </div>
        <div id='about'>
            <h3>About</h3>
            All of my open-source projects are located on my GitHub profile. Feel free to grab my public key; it's what I sign my emails with. 
        </div>
        <div id='links'>
            <h3>Projects to Follow</h3>
            <a href='https://github.com/InsidiousMind/Gomoku'>Gomoku!</a><br/>
            Gomoku is a networked game hosted by <a href='https://github.com/InsidiousMind'>InsidiousMind</a>. We wrote a server/client application in C and Python to play a five-in-a-row game with an integrated chat system. We haven't looked at it in a while, so parts may not work so well.
                <br/><br/>
            <a href='https://keybase.io'>Keybase</a><br/>
            Keybase is a project that hopes to bring crypto to everyone - not just programmers. It bundles encrypted filesharing and chat with identity proofs and easy key sharing in hopes of bringing back the golden age of public key cryptography.
            <br/><br/>
            <a href='https://python.org'>Python</a><br/>
            Python is an open-source scripting language built to be fast, expressive, and adaptable to just about any use case.
            <br/><br/>
            <a href='https://ruby-lang.org'>Ruby</a><br/>
            Ruby is an open-source scripting language built to make up for everything other languages lack.
            <br/><br/>
            <a href='https://djangoproject.org'>Django</a><br/>
            Django is the web framework for perfectionists with deadlines. You can view a Django project that I contribute to <a href='https://github.com/cyclerdan/Projtrack3'>here</a>.
            <br/><br/>
            <a href='akvantaAbout.html'>Akvanta</a><br/>
            Akvanta is a painfully minimalist web game I wrote a couple years ago as my introduction to ECMAScript. It's optimized for mobile devices - kind of.
            <br/><br/>
        </div>
        <div id='sidebar'>
            <p>
            <a href="https://github.com/Romulus10">Romulus10 on GitHub</a><br/><br/>
            <a href="https://keybase.io/romulus10">Romulus10 on Keybase</a><br/><br/>
            <a href="mailto:romulus108@protonmail.com">Email</a><br/><br/>
            <a href='romulus10.gpg'>GPG Public Key</a><br/><br/>
            <a href='https://romulus10.github.io'>Home</a><br/><br/>
            <a href='https://romulus10.github.io/RomulusBlog'>Blog</a><br/><br/>
        </div>
            </p> 
        </div>
        <div id='footer'>
            <table id='foot_table'>
                <tr>
                    Views: <?php exec("python counter.py"); $file=fopen("count.txt", "r");echo fgets($file);fclose($file); ?>
                </tr>
            </table>
        </div>
    </body>
</html>
