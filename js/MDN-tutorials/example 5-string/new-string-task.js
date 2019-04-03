//var myString="MAN675847583748sjt567654;Manchester Piccadilly"
var myString="LIV5hg65hd737456236dch46dg4;Liverpool Lime Street"
var finalString=myString.slice(0,3)
console.log(finalString)
var whereToCut=myString.indexOf(";")
console.log(whereToCut)
console.log(finalString.concat(":",myString.slice(whereToCut+1)))
