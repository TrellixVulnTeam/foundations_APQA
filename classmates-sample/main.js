var myButton = document.getElementById("submit");
	submit.onclick = function (){
		var node = document.createElement("LI");
		var classmate_name = document.getElementById("classmate_name").value
  		var textnode = document.createTextNode(classmate_name);
  		node.appendChild(textnode);
  		document.getElementById("myList").appendChild(node);
}



