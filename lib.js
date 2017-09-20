function random_comic() {
    var comics = new Array('xkcd/7_eleven.png', 'xkcd/existence_proof.png', 'xkcd/hacking.png', 'xkcd/machine_learning.png', 'xkcd/who.png', 'xkcd/borrow_your_laptop.png', 'xkcd/existential_bug_reports.png', 'xkcd/here_to_help.png', 'xkcd/pointers.png', 'xkcd/color_pattern.png', 'xkcd/genetic_testing_results.png', 'xkcd/hottest_editors.png', 'xkcd/still_in_use.png');
    var rand_num = Math.floor(13*Math.random());
    var xkcd_comic = document.getElementById('xkcd_comic').setAttribute('src', comics[rand_num]);
}

function go_home() {
    window.location = 'index.html';
}

function link_page() {
    window.location = 'links.html';
}

function load_page() {
    if (document.getElementById('xkcd') != undefined) {
        random_comic();
    }
    if (document.getElementById('welcome') != undefined){
            if (typeof(Storage) !== 'undefined') {
            if (localStorage.visited == 'true') {
                document.getElementById('welcome').innerHTML = 'Welcome back.';
            } else {
                document.getElementById('welcome').innerHTML = 'Welcome!';
                localStorage.setItem('visited', 'true');
            }
        } else {
            document.getElementById('welcome').innerHTML = 'Welcome!';
        }
    }
}
