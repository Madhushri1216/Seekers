$("#submit").click(function() {
	if($("#txtName").val() == "") {
		alert("Please Enter Name");
		$("#txtName").focus();
		return false;
	}

	if($("#college").val() == "") {
		alert("Please Enter College.");
		$("#college").focus();
		return false;
	}

	if($("#email").val() == "") {
		alert("Please Enter Your Email.");
		$("#email").focus();
		return false;
	}

	if($("#contact").val() == "") {
		alert("Please Enter contact number");
		$("#contact").focus();
		return false;
	}
});