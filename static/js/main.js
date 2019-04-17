setTimeout(function() {
  $("#messages").fadeOut("slow");
}, 3000);

function changeTicketStatus(val, id, csrf_token) {

  $.ajax({
    url: "/tickets/updateticketstatus/"+id+"/",
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token,
      ticket_status: val
    },
    success: function(result) {}
  });
}
