$("#addbtn").click (function(){

	if($("#nameText").val() == "") {
		alert("Please Enter college Name");
		$("#nameText").focus();
		return false;
	}
	if($("#nameUni").val() == "") {
		alert("Please Enter college University");
		$("#nameUni").focus();
		return false;
	}
	if($("#nameLoc").val() == "") {
		alert("Please Enter Location");
		$("#nameLoc").focus();
		return false;
	}
	if($("#number").val() == "") {
		alert("Please Enter Contact no");
		$("#number").focus();
		return false;
	}
	if($("#email").val() == "") {
		alert("Please Enter Email adress");
		$("#email").focus();
		return false;
	}
	if($("#password").val() == "") {
		alert("Please Enter Password");
		$("#password").focus();
		return false;
	}
});