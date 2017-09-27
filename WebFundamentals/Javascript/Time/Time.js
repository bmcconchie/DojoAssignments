var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

function TellTime() {
    var time;
    var relation;
    if (PERIOD === "PM") {
        time = "in the evening."
    } else {
        time = "in the morning."
    }
    if (MINUTE > 30) {
        HOUR += 1;
        relation = "almost"
    } else {
        relation = "just after"
    }
    console.log("The time is " + relation + " " + HOUR + " " + time)

}
TellTime()