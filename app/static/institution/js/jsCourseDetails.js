function alphaOnly(event) {
  var key = event.which ? event.which : event.keyCode;
  return (
    (key >= 65 && key <= 90) ||
    key == 8 ||
    (event.charCode >= 97 && event.charCode <= 122) ||
    event.charCode == 32
  );
}
function isNumberKey(evt) {
  var charCode = (evt.which) ? evt.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
    
    return false;
  }
  return true;
}
$("#btn_add").click(function () {

  if ($("#txtName").val() == "") {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if ($("#txtFees").val() == "") {
    alert("Please Enter Fees");
    $("#txtFees").focus();
    return false;
  }

  // if($("#txtTotalSeatsGovernment").val() == "") {
  // 	alert("Please Enter Total Government Seats");
  // 	$("#txtTotalSeatsGovernment").focus();
  // 	return false;
  // }


  // if($("#txtTotalSeatsManagement").val() == "") {
  //   alert("Please Enter Total Management Seats");
  //   $("#txtTotalSeatsManagement").focus();
  //   return false;
  // }
  var formData = new FormData();
  //   var lclFile = document.getElementById("selImage");
  //   lclImage = lclFile.files[0];

  formData.append("txtName", $("#txtName").val());
  formData.append("txtFees", $("#txtFees").val());
  // formData.append("txtTotalSeatsGovernment", $("#txtTotalSeatsGovernment").val());
  // formData.append("txtTotalSeatsManagement", $("#txtTotalSeatsManagement").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/course_institution_details/",
    type: "POST",
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

    if ($("#txtName1").val() == "") {
      alert("Please Enter Name");
      $("#txtName1").focus();
      return false;
    }
    if ($("#txtFees1").val() == "") {
      alert("Please Enter Fees");
      $("#txtFees1").focus();
      return false;
    }
    // if($("#txtTotalSeats1").val() == "") {
    //   alert("Please Enter Mail Id");
    //   $("#txtTotalSeats1").focus();
    //   return false;
    // }

    var formData = new FormData()
    formData.append("txtName1", $("#txtName1").val());
    formData.append("txtFees1", $("#txtFees1").val());
    // formData.append("txtTotalSeats1", $("#txtTotalSeats1").val());
    // formData.append("txtTotalSeatsGovernment1", $("#txtTotalSeatsGovernment1").val());
    // formData.append("txtTotalSeatsManagement1", $("#txtTotalSeatsManagement1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");


    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/course_institution_details/",
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

      url: "/course_institution_details/",
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

    url: "/course_institution_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {

      console.log(response);
      // $("#dataTables-example tr:gt(0)").remove();
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;

        $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].ic_id + '</td><td>' + response[i].ic_institute_name + '</td><td>' + response[i].ic_fees + '</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-bs-toggle="modal" data-bs-target="#edit_modal"  class="text-primary" onClick="getRowsUpdate();">Edit</a><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>');
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {

    },
  });

}

function getRowsUpdate() {
  $("#tableData tr").click(function () {
    var currentRow = $(this).closest("tr");
    var lclID = currentRow.find("td:eq(1)").text();
    var lclName = currentRow.find("td:eq(2)").text();
    var lclMobile = currentRow.find("td:eq(3)").text();
    // var lclEmail = currentRow.find("td:eq(4)").text();
    // alert(lclID);  
    $("#txtName1").val(lclName);
    $("#txtFees1").val(lclMobile);
    // $("#txtTotalSeats1").val(lclEmail);.
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
