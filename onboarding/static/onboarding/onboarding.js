window.onload = function() {
    (function() {
        jQuery.noConflict();
        formdata = new FormData();

        function userMedia() {
            return navigator.getUserMedia = navigator.getUserMedia ||
                navigator.webkitGetUserMedia ||
                navigator.mozGetUserMedia ||
                navigator.msGetUserMedia || null;

        }

        if (userMedia()) {
            var videoPlaying = false;
            var constraints = {
                video: true,
                audio: false
            };

            var media = navigator.getUserMedia(constraints, function(stream) {
                var v = document.getElementById('v');

                var url = window.URL || window.webkitURL;

                v.src = url ? url.createObjectURL(stream) : stream;

                // Start the video
                v.play();
                videoPlaying = true;
            }, function(error) {
                console.log("ERROR");
                console.log(error);
            });

            // Listen for user click on the "take a photo" button
            document.getElementById('take').addEventListener('click', function() {
                if (videoPlaying) {
                    var canvas = document.getElementById('canvas');
                    canvas.width = v.videoWidth;
                    canvas.height = v.videoHeight;
                    canvas.getContext('2d').drawImage(v, 0, 0);

                    var data = canvas.toDataURL('image/png');
                    document.getElementById('photo').setAttribute('src', data);
                    if (formdata) {
                        formdata.append("csrfmiddlewaretoken", window.CSRF_TOKEN);
                        formdata.append("image", data);   
                    }
                }
            }, false);

            document.getElementById('subButton').addEventListener('click', function() {

                if (formdata && document.getElementById('photo').getAttribute('src') != "") {
                    jQuery.ajax({
                        url: "liste/",
                        type: "POST",
                        data: formdata,
                        processData: false,
                        contentType: false,
                        success: function() { alert("success"); }
                    });        
                }
            }, false);
        } else {
            console.log("Browser does not support WebCam integration");
        }
    })();
}