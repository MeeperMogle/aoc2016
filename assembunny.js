const memory = {
    a: 0,
    b: 0,
    c: 0,
    d: 0,
};

// If input is not number, translate to number found in that MEMORY ADDRESS instead
function getRealNumber(number) {
    if (Number.isInteger(parseInt(number))) {
        return parseInt(number);
    } else {
        return parseInt(memory[number]);
    }
}

// Put x into memory address y
function cpy(x, y) {
    memory[y] = getRealNumber(x);
}

// Increment on address by 1
function inc(x) {
    memory[x]++;
}

// Decrement on address by 1
function dec(x) {
    memory[x]--;
}

// Return new index position
function jnz(x, relativeSteps, currentIndex) {
    // Only manipulate if x !== 0
    if (getRealNumber(x) !== 0) {
        return parseInt(currentIndex += relativeSteps);
    } else {
        return parseInt(currentIndex);
    }
}
