window.onload = function() {
    (function() {
        jQuery.noConflict();
        var formdata = new FormData();
        var state = "front";

        document.getElementById('subButton').style.display = "none";
        document.getElementById('userData').style.display = "none";
        document.getElementById('confPicture').style.display = "none";
        document.getElementById('front_layout').style.display = "block";


        window.onbeforeunload = function() {
            var txt;
            var r = confirm("Are you sure you want to refresh the page? Your registration will not be taken into account");
            if (r == true) {
                txt = "You pressed OK!";
            } else {
                txt = "You pressed Cancel!";
            }
        }

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
            }
        }

        function selectPicture() {
            var imgData = document.getElementById('photo').getAttribute('src');
            //console.log(imgData);
            if(state == "front") {
                localStorage.setItem("frontData", imgData);
            } else {
                localStorage.setItem("backData", imgData);
            }
        }

        function uploadDocs() {
            if (formdata) {
                formdata.append("csrfmiddlewaretoken", window.CSRF_TOKEN);
                //formdata.append("frontImage", localStorage.getItem("frontData"));   
                formdata.append("backImage", localStorage.getItem("backData")); 
                formdata.append("state", "first");  
                jQuery.ajax({
                        url: "/onboarding/doc_scan/",
                        type: "POST",
                        data: formdata,
                        processData: false,
                        contentType: false,
                        success: function(data, status, xhttp) {
                            console.log(status);
                            if(data.response) {

                                //localStorage.setItem("userData", JSON.stringify(data.response));
                                var user = JSON.parse(data.response);

                                document.getElementById('subButton').style.display = "none";
                                document.getElementById('side').style.display = "none";
                                document.getElementById('v').style.display = "none";
                                document.getElementById('overlay').style.display = "none";
                                document.getElementById('canvas').style.display = "none";
                                document.getElementById('bump').style.display = "none";
                                document.getElementById('photo').style.display = "none";
                                document.getElementById('take').style.display = "none";
                                document.getElementById('spacebarRec').style.display = "none";
                                document.getElementById('confPicture').style.display = "none";
                                document.getElementById('form').style.display = "none";
                                document.getElementById('userData').style.display = "block";
                                document.getElementById('instructions').innerHTML = "Please fill the form with your informations";
                                document.getElementById('photo').setAttribute('src', '');

                                fnameItem = document.getElementById('fnameForm');
                                lnameItem = document.getElementById('lnameForm');
                                nationalityItem = document.getElementById('nationalityForm');
                                doeItem = document.getElementById('doeForm');
                                dobItem = document.getElementById('dobForm');
                                sexItem = document.getElementById('sexForm');
                                dniItem = document.getElementById('dniForm');

                                fnameItem.value = user.first_name;
                                lnameItem.value = user.last_name;
                                nationalityItem.value = user.nationality;
                                doeItem.value = user.doe;
                                dobItem.value = user.dob;
                                sexItem.value = user.sex;
                                dniItem.value = user.dni;

                            } else if(data.error_msg) {
                                document.getElementById('errorHandling').style.display = "block";
                                document.getElementById('errorHandling').innerHTML = data.error_msg;
                                state = "front";
                                document.getElementById('side').innerHTML = "Please scan the front side of your card";
                                document.getElementById('back_layout').style.display = "none";
                                document.getElementById('front_layout').style.display = "block";
                                document.getElementById('confPicture').style.display = "none";
                                document.getElementById('testPhoto').setAttribute('src', '');
                                document.getElementById('photo').setAttribute('src', '');
                                document.getElementById('take').style.marginTop = "600px";
                            }
                        }
                 });
            }
        }

        // Listen for user click on the "take a photo" button
        document.getElementById('take').addEventListener('click', function() {
            capture();
            document.getElementById('confPicture').style.display = "block";
        }, false);

        document.addEventListener("keypress", function(event) {
            if (event.keyCode == 32 && event.target == document.body) {
                event.preventDefault();
                capture();
                document.getElementById('confPicture').style.display = "block";
            }
        })

        document.getElementById('subButton').addEventListener('click', function() {
            if (formdata && document.getElementById('photo').getAttribute('src') != "") {
                jQuery.ajax({
                    url: "onboarding/doc_scan/",
                    type: "POST",
                    data: formdata,
                    processData: false,
                    contentType: false,
                    success: function() { alert("success"); }
                });        
            }
        }, false);

        document.getElementById('confPicture').addEventListener('click', function() {
            selectPicture();
            //document.getElementById('testPhoto').setAttribute('src', localStorage.getItem("frontData"));
            if(state == "front") {
                state = "back";
                document.getElementById('side').innerHTML = "Please scan the back side of your card";
                document.getElementById('front_layout').style.display = "none";
                document.getElementById('back_layout').style.display = "block";
                document.getElementById('confPicture').style.display = "none";
                document.getElementById('testPhoto').setAttribute('src', '');
                document.getElementById('photo').setAttribute('src', '');
                document.getElementById('take').style.marginTop = "600px";
                document.getElementById('errorHandling').innerHTML = '';
            } else if(state == "back") {
                uploadDocs();
            }
        }, false);
    })();
}