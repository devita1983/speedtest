const speedTest = require("speedtest-net");

const test = speedTest({maxTime: 5000});

test.on("data", data => {
  console.log(data.speeds);
});

test.on("error", error => {
  console.error(error);
});
