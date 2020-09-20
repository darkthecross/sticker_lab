var img_data = null;

function encodeImageFileAsURL(element) {
    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function() {
        img_data = reader.result;
    }
    reader.readAsDataURL(file);
}

document.getElementById('submit_btn').addEventListener("click", function() {
    $.ajax({
        type: "POST",
        url: "/img_process",
        data: {'img_data': img_data},
        success: function(data) {console.log(data);},
        dataType: "json"
      });
});