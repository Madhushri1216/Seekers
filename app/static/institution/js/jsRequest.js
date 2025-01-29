
$(document).ready(function () {

  //Edit modal submit click
  $(document).on("click", "#btn_accept", function () {
   

    let formData = new FormData();

    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "Accepted");

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/get_institute_update_request/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Details Updated Succesfully");
        location.reload();
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

  $(document).on("click", "#btn_reject", function () {

    let formData = new FormData();

    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "Rejected");

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/get_institute_update_request/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Details Updated Succesfully");
        location.reload();
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


});


function getAdminMasterData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

    url: "/get_institute_request/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {

      // console.log(response);
      // $("#dataTables-example tr:gt(0)").remove();
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;
        if(response[i].ir_status == "Accepted" && response[i].ir_payment_status == "Success") {
        $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].ir_id + '</td><td>' + response[i].ir_department + '</td><td>' + response[i].ir_name + '</td><td>' + response[i].ir_email + '</td><td>' + response[i].ir_mobile + '</td><td>' + response[i].ir_address + '</td><td>' + response[i].ir_percentage + '</td><td>' + response[i].ir_previous_education + '</td><td>' + response[i].ir_year_passing + '</td><td>' + response[i].ir_status + '</td><td>' + response[i].ir_payment_status + '</td><td>' + response[i].ir_amount );
      }else if(response[i].ir_status == "Rejected") {
        $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].ir_id + '</td><td>' + response[i].ir_department + '</td><td>' + response[i].ir_name + '</td><td>' + response[i].ir_email + '</td><td>' + response[i].ir_mobile + '</td><td>' + response[i].ir_address + '</td><td>' + response[i].ir_percentage + '</td><td>' + response[i].ir_previous_education + '</td><td>' + response[i].ir_year_passing + '</td><td>' + response[i].ir_status + '</td><td>' + response[i].ir_payment_status + '</td><td>' + response[i].ir_amount + '</td><td><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Process</a></div></td></tr>');
     } 
     else {
       $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].ir_id + '</td><td>' + response[i].ir_department + '</td><td>' + response[i].ir_name + '</td><td>' + response[i].ir_email + '</td><td>' + response[i].ir_mobile + '</td><td>' + response[i].ir_address + '</td><td>' + response[i].ir_percentage + '</td><td>' + response[i].ir_previous_education + '</td><td>' + response[i].ir_year_passing + '</td><td>' + response[i].ir_status + '</td><td>' + response[i].ir_payment_status + '</td><td>' + response[i].ir_amount + '</td><td><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Process</a></div></td></tr>');
     }
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
    var lclDept = currentRow.find("td:eq(3)").text();
    var lclDesg = currentRow.find("td:eq(4)").text();
    // alert(lclID);  
    $("#txtName1").val(lclName);
    $("#txtDepartment1").val(lclDept);
    $("#txtDesignation1").val(lclDesg);
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
