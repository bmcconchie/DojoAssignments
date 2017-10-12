function Node(value) {
    this.value = value;
    this.next = null
}

function Sll() {
    this.head = null;
}

var list1 = new Sll();
var node1 = new Node(2);
list1.head = node1;