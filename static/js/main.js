setTimeout(function() {
  $("#messages").fadeOut("slow");
}, 3000);

function changeTicketStatus(val, id, csrf_token) {
  $.ajax({
    url: "/tickets/updateticketstatus/" + id + "/",
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token,
      ticket_status: val
    },
    success: function(result) {
      $("#statusCheck")
        .show()
        .html('<i class="fas fa-check"></i>')
        .fadeOut(4000);
    }
  });
}

function voteOnTicket(id, csrf_token) {
  $("#vote-form").submit(function(e) {
    e.preventDefault();
  });

  $.ajax({
    url: "/tickets/addvote/" + id + "/",
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token
    },
    success: function(result) {
      $("#votes-number").text(result.numVotes);
      alert(result.msg);
    }
  });
}

function openImage(imageUrl) {
  var modal = document.getElementById("image-modal");
  var modalImg = document.getElementById("bug-image");

  modal.style.display = "block";
  modalImg.src = imageUrl;

  setTimeout(function() {
  // When the user clicks anywhere, close the modal
    document.addEventListener('click', function() {
      modal.style.display = "none";
    }, 500);
  })
  
}
