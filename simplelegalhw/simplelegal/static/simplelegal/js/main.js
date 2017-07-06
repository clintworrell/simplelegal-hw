$("#filter-results-input").keyup(function() {
  var searchTerm = $("#filter-results-input").val();
  $.ajax({
    url: `./filter=${searchTerm}/`,
    success: function(response) {
      $("#invoices-table").replaceWith(response);
    }
  });
});
