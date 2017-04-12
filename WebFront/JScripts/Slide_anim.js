/**
 * Created by Bogdan on 10.04.2017.
 */
function getOffset( el ) {
    var _x = 0;
    var _y = 0;
    while( el && !isNaN( el.offsetLeft ) && !isNaN( el.offsetTop ) ) {
        _x += el.offsetLeft - el.scrollLeft;
        _y += el.offsetTop - el.scrollTop;
        el = el.offsetParent;
    }
    return { top: _y, left: _x };
}



function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}


function Silky_random_move(e1) {
    var elem = document.getElementById(e1);
    var x, xb;
    var y, yb;

    elem.style.position= 'absolute';

    var elemB = document.body;
    var pos=30;
    y=getOffset(e1).top;
    elem.style.top=(y+320)+'px';

    xb = elemB.scrollWidth;
    var id = setInterval(frame, 5);


    function frame() {
        if (pos == (xb-200)) {
            clearInterval(id);
            elem.style.visibility='hidden';
            elem.style.left = pos + 'px';
            var rnumb=randomIntFromInterval(1,4);
            var rimg='im'+rnumb;
            Silky_random_move(rimg);

        } else {
            pos++;
            elem.style.left = pos + 'px';
            elem.style.visibility='visible';
        }
    }
}