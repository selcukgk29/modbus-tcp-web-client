$(document).ready(function () {
  $(".edit-on-click").click(function () {
    var $text = $(this),
      $input = $('<input type="text" />');
    $text.hide().after($input);
    $(".controls-update").show();
    $input
      .val($text.html())
      .show()
      .focus()
      .keypress(function (e) {
        var key = e.which;
        if (key == "13") {
          // enter key
          $input.hide();
          $text.html($input.val()).show();
          $.get("/api", { writeRegister: $input.val() }, function (data) {
            console.log(data);
          });
          return false;
        }
      })
      .focusout(function () {
        $input.remove();
        $text.show();
      });
  });
  $(".controls-update").click(function () {
    $(".controls-update").hide();
  });

  $("#slider").roundSlider({
    radius: 85,
    width: 8,
    handleSize: "+32",
    handleShape: "dot",
    sliderType: "min-range",
    value: 25,
    change: function (event) {
      $.get("/api", { roundSliderData: event.value }, function (data) {
        console.log(event.value);
      });
    },
  });
});
