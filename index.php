<!DOCTYPE html>
<html>
    <head>
         <meta charset='utf-8'/>
        <link rel='stylesheet' type='text/css' href='style.css'>
        <title>Home</title>
        <!-- Global Site Tag (gtag.js) - Google Analytics -->
        <script async src='https://www.googletagmanager.com/gtag/js?id=UA-44434564-5'></script>
        <script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments)};
gtag('js', new Date());

gtag('config', 'UA-44434564-5');
        </script>
        <script src='lib.js'></script>
    </head>
    <body onLoad='load_page()'>
    <div id='menu'>
        <button class='dropbtn' onclick='go_home()'>Home</button>
        <button class='dropbtn' onclick='link_page()'>Projects to Follow</button>
        <div class='dropdown'>
            <button class='dropbtn'>Links</button>
            <div class='dropdown-content'>
                <a href='https://github.com/Romulus10'>Romulus10 on GitHub</a><br/><br/>
                <a href='https://keybase.io/romulus10'>Romulus10 on Keybase</a><br/><br/>
                <a href='mailto:romulus108@protonmail.com'>Email</a><br/><br/>
                <a href='romulus10.gpg'>GPG Public Key</a><br/><br/>
                <a href='index.php'>Home</a><br/><br/>
            </div>
        </div>
    </div><br/>
    <div id='welcome'></div>
    <br/>
        <div id='xkcd'>
            <a href='https://www.xkcd.com/'>
                <img src='' alt='XKCD' id='xkcd_comic'>
            </a>
        </div>
        <div id='about'>
            <h3>About</h3>
            All of my open-source projects are located on my GitHub profile. Feel free to <a href='romulus10.gpg'>grab my public key;</a> it's what I sign my emails with.
        </div>
        </div>
        <div id='footer'>
            <table id='foot_table'>
                <tr>
                </tr>
            </table>
        </div>
    </body>
</html>
