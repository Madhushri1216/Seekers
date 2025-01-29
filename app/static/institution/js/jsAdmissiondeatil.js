$("#submit").click(function() {
	if($("#txtName").val() == "") {
		alert("Please Enter Name");
		$("#txtName").focus();
		return false;
	}

	if($("#Middlename").val() == "") {
		alert("Please Enter Middlename.");
		$("#Middlename").focus();
		return false;
	}

	if($("#Lastname").val() == "") {
		alert("Please Enter Your Lastname.");
		$("#Lastname").focus();
		return false;
	}

	if($("#contact").val() == "") {
		alert("Please Enter contact number");
		$("#contact").focus();
		return false;
	}

	if($("#address").val() == "") {
		alert("Please Enter Address");
		$("#address").focus();
		return false;
	}

	if($("#email").val() == "") {
		alert("Please Enter email");
		$("#email").focus();
		return false;
	}

	if($("#pass").val() == "") {
		alert("Please Enter Your Password");
		$("#pass").focus();
		return false;
	}

	if($("#repass").val() == "") {
		alert("Please Re-enter Your Password");
		$("#repass").focus();
		return false;
	}
});