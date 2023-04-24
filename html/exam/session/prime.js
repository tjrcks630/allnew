onmessage = function (e) {
    let num = 0;
    let i = 0;

    if (num === 1) {
        return false;
    }

    if (num === 2) {
        return true;
    }


    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }



    return true;
}

