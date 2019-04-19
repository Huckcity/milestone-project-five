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
    success: function(result) {
      // alert('Status Updated');
      $('#statusCheck')
        .show()
        .html('<i class="fas fa-check"></i>')
        .fadeOut(4000);
      
    }
  });
}

function voteOnTicket(id, csrf_token) {

  $("#voteForm").submit(function(e){
    e.preventDefault();
  });

  $.ajax({
    url: "/tickets/addvote/"+id+"/",
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token,
    },
    success: function(result) {
      // alert('Status Updated');
      $('#votesNumber').text(result.numVotes);
      alert(result.msg)
    }
  });
}