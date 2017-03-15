window.onload = function() {
    (function() {
        function userMedia() {
            return navigator.getUserMedia = navigator.getUserMedia ||
                navigator.webkitGetUserMedia ||
                navigator.mozGetUserMedia ||
                navigator.msGetUserMedia || null;

        }

        // Now we can use it
        if (userMedia()) {
            var videoPlaying = false;
            var constraints = {
                video: true,
                audio: false
            };

            var media = navigator.getUserMedia(constraints, function(stream) {
                var v = document.getElementById('v');

                // URL Object is different in WebKit
                var url = window.URL || window.webkitURL;

                // create the url and set the source of the video element
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
                    var data = canvas.toDataURL('image/webp');
                    document.getElementById('photo').setAttribute('src', data);
                }
            }, false);
        } else {
            console.log("Browser does not support WebCam integration");
        }
    })();
}