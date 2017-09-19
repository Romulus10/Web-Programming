function random_comic() {
    var comics = new Array('xkcd/7_eleven.png', 'xkcd/existence_proof.png', 'xkcd/hacking.png', 'xkcd/machine_learning.png', 'xkcd/who.png', 'xkcd/borrow_your_laptop.png', 'xkcd/existential_bug_reports.png', 'xkcd/here_to_help.png', 'xkcd/pointers.png', 'xkcd/color_pattern.png', 'xkcd/genetic_testing_results.png', 'xkcd/hottest_editors.png', 'xkcd/still_in_use.png');
    var rand_num = Math.floor(13*Math.random());
    var xkcd_comic = document.getElementById('xkcd_comic').setAttribute('src', comics[rand_num]);
}

function go_home() {
    window.location = "http://www.cs.scranton.edu/~batzels2/";
}

function load_page() {
    random_comic();
}
