$("#btn_add").click(function() {

  if($("#selUniversity").val() == "") {
    alert("Please Select University");
    $("#selUniversity").focus();
    return false;
  }

  if($("#selImage").val() == "") {
    alert("Please Select Image");
    $("#selImage").focus();
    return false;
  }

	if($("#txtName").val() == "") {
		alert("Please Enter Name");
		$("#txtName").focus();
		return false;
	}
	if($("#txtContact").val() == "") {
		alert("Please Enter Contact Number");
		$("#txtContact").focus();
		return false;
	}
	if($("#txtEmail").val() == "") {
		alert("Please Enter Mail Id");
		$("#txtEmail").focus();
		return false;
	}

  if($("#txtAddress").val() == "") {
    alert("Please Enter Address");
    $("#txtAddress").focus();
    return false;
  }

	if($("#txtAbout").val() == "") {
		alert("Please Enter About");
		$("#txtAbout").focus();
		return false;
	}
	if($("#txtNaac").val() == "") {
		alert("Please Enter About");
		$("#txtNaac").focus();
		return false;
	}

  if($("#selRank").val() == "") {
    alert("Please Select Rank");
    $("#selRank").focus();
    return false;
  }


	var formData = new FormData();
  var lclFile = document.getElementById("selImage");
  lclImage = lclFile.files[0];

  formData.append("lclImage", lclImage);
  formData.append("selUniversity", $("#selUniversity").val());
  formData.append("txtName", $("#txtName").val());
  formData.append("txtContact", $("#txtContact").val());
  formData.append("txtEmail", $("#txtEmail").val());
  formData.append("txtAddress", $("#txtAddress").val());
  formData.append("txtAbout", $("#txtAbout").val());
  formData.append("selRank", $("#selRank").val());
  formData.append("txtNaac", $("#txtNaac").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/college_details/",
    type: "POST",
    // headers: {'X-CSRFToken': '{{ csrf_token }}'},
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {

      alert("Details Added Successfully");
      location.reload();
      table.ajax.reload();
      $("#add_modal").modal('hide');

    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});

$(document).ready(function () {

  //Edit modal submit click
  $(document).on("click", "#btn_update", function () {
    // alert("hi");

  if($("#txtName").val() == "") {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }
  if($("#txtContact").val() == "") {
    alert("Please Enter Contact Number");
    $("#txtContact").focus();
    return false;
  }
  if($("#txtEmail").val() == "") {
    alert("Please Enter Mail Id");
    $("#txtEmail").focus();
    return false;
  }

  if($("#txtAddress").val() == "") {
    alert("Please Enter Address");
    $("#txtAddress").focus();
    return false;
  }

  if($("#txtAbout").val() == "") {
    alert("Please Enter About");
    $("#txtAbout").focus();
    return false;
  }
  if($("#txtNaac1").val() == "") {
		alert("Please Enter About");
		$("#txtNaac1").focus();
		return false;
	}

  if($("#selRank1").val() == "") {
    alert("Please Select Rank");
    $("#selRank1").focus();
    return false;
  }

    var formData = new FormData();
    formData.append("selUniversity1", $("#selUniversity1").val());
    formData.append("txtName1", $("#txtName1").val());
    formData.append("txtContact1", $("#txtContact1").val());
    formData.append("txtEmail1", $("#txtEmail1").val());
    formData.append("txtAddress1", $("#txtAddress1").val());
    formData.append("txtAbout1", $("#txtAbout1").val());
    formData.append("selRank1", $("#selRank1").val());
    formData.append("txtNaac1", $("#txtNaac1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");


    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/college_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Details Updated Succesfully");
        location.reload();
        table.ajax.reload();
        $("#edit_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });

  //Delete work step
  $(document).on("click", "#btn_delete", function () {

    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete");


    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },

      url: "/college_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Details deleted succesfully");
        location.reload();
        table.ajax.reload();
        $("#delete_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        // Reset Form
        //$("#view_field_form")[0].reset();
        $(".close").click();
      },
    });
  });

});


function getAdminMasterData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");


  $.ajax({

    url: "/college_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {

      console.log(response);
      // $("#dataTables-example tr:gt(0)").remove();
      for (let i = 0; i < response.length; i++) {
        let j = i + 1;
        
        $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].cl_id + '</td><td>' + response[i].cl_university_name + '</td><td>' + response[i].cl_name + '</td><td>' + response[i].cl_mobile + '</td><td>' + response[i].cl_email + '</td><td>' + response[i].cl_address + '</td><td>' + response[i].cl_about + '</td><td>' + response[i].cl_naac + '</td><td>' + response[i].cl_rank + '</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-bs-toggle="modal" data-bs-target="#edit_modal"  class="text-primary" onClick="getRowsUpdate();">Edit</a><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>');
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {

    },
  });

}

function getUniversityData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

    url: "/university_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {

      console.log(response);
      // $("#dataTables-example tr:gt(0)").remove();
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;
        
        $("#selUniversity").append('<option value="'+response[i].un_name+'">'+response[i].un_name+'</option>');
        $("#selUniversity1").append('<option value="'+response[i].un_name+'">'+response[i].un_name+'</option>');
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {

    },
  });

}

getUniversityData();

function getRowsUpdate() {
  $("#tableData tr").click(function () {
    var currentRow = $(this).closest("tr");
    var lclID = currentRow.find("td:eq(1)").text();
    var lclUniversity = currentRow.find("td:eq(2)").text();
    var lclName = currentRow.find("td:eq(3)").text();
    var lclMobile = currentRow.find("td:eq(4)").text();
    var lclEmail = currentRow.find("td:eq(5)").text();
    var lclAddress = currentRow.find("td:eq(6)").text();
    
    // var lclTotalCollege = currentRow.find("td:eq(6)").text();
    var lclAbout = currentRow.find("td:eq(7)").text();
    var lclNaac = currentRow.find("td:eq(8)").text();
    var lclRank = currentRow.find("td:eq(9)").text();
    // alert(lclUniversity);  
    $("#selUniversity1").val(lclUniversity);
    $("#txtName1").val(lclName);
    $("#txtContact1").val(lclMobile);
    $("#txtEmail1").val(lclEmail);
    $("#txtAddress1").val(lclAddress);
    // $("#txtTotalColleges1").val(lclTotalCollege);
    $("#txtAbout1").val(lclAbout);
    $("#txtNaac1").val(lclNaac);
    $("#selRank1").val(lclRank);
    $("#edit_id").val(lclID);

  });
}


function getRowsDelete() {
  $("#tableData tr").click(function () {
    var currentRow = $(this).closest("tr");
    var lclID = currentRow.find("td:eq(1)").text();
    // alert(lclID);
    $("#delete_id").val(lclID);

  });
}

getAdminMasterData()
