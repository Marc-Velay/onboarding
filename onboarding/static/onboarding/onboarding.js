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
        //////////////Legacy support code/////////////////
        if (navigator.mediaDevices === undefined) {
            navigator.mediaDevices = {};
        }
        if (navigator.mediaDevices.getUserMedia === undefined) {
            navigator.mediaDevices.getUserMedia = function(constraints) {
                var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
                if (!getUserMedia) {
                    return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
                }
                return new Promise(function(resolve, reject) {
                    getUserMedia.call(navigator, constraints, resolve, reject);
                });
            }
        }
        //////////////////////////////////////////////////

        navigator.mediaDevices.getUserMedia({ audio: false, video: true }).then(function(mediaStream) {
            var v = document.getElementById('v');
            var video = document.querySelector('video');
            if ("srcObject" in video) {
                video.srcObject = mediaStream;
            } else {
                video.src = window.URL.createObjectURL(mediaStream);
            }
            video.onloadedmetadata = function(e) {
                var can = document.getElementById('overlay');
                var bump = document.getElementById('bump');
                video.play();

                videoPlaying = true;
                can.style.position = "absolute";
                v.style.position = "absolute";
                //can.style.width = v.videoWidth + "px";
                //can.style.height = v.videoHeight + "px";
                //bump.style.marginBottom = v.videoHeight + "px";
            };
        }).catch(function(error) {
            console.log("ERROR");
            console.log(error);
        });

        function capture() {
            if (videoPlaying) {
                var bump = document.getElementById('take');
                var canvas = document.getElementById('canvas');
                bump.style.marginTop = "30px";
                canvas.width = 800;
                canvas.height = 600;
                canvas.getContext('2d').drawImage(v, 0, 0, 800, 600);

                var data = canvas.toDataURL('image/png');
                document.getElementById('photo').setAttribute('src', data);
                if (formdata) {
                    formdata.append("csrfmiddlewaretoken", window.CSRF_TOKEN);
                    formdata.append("image", data);   
                }
            }
        }

        // Listen for user click on the "take a photo" button
        document.getElementById('take').addEventListener('click', function() {
            capture();
        }, false);

        document.addEventListener("keypress", function(event) {
            if (event.keyCode == 32 && event.target == document.body) {
                event.preventDefault();
                capture();
            }
        })

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
    })();
}