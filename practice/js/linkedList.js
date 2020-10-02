function node(value) {
    this.value = value;
    this.link = null;
}

let start = new node(0);

for (var i = 1; i < 5; i++) {
    let temp = new node(i);
    temp.link = start;
    start = temp;
}

let p = start;
while (p) {
    console.log(p.value);
    p = p.link;
}
