console.log(
  require("fs")
    .readFileSync("./output.txt", "utf8")
    .trim()
    .split(" \n")
    .map((e) => String.fromCharCode(e))
    .join("")
);
