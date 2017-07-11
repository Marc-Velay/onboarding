window.onload = function() {
    (function() {
        jQuery.noConflict();
        var formdata = new FormData();
        var state = "front";

        document.getElementById('subButton').style.display = "none";
        //document.getElementById('userData').style.display = "none";
        document.getElementById('usercontact_form').style.display = "none";
        document.getElementById('confPicture').style.display = "none";
        document.getElementById('front_layout').style.display = "block";

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
            };
        }).catch(function(error) {
            console.log("ERROR");
            console.log(error);
        });

        function capture() {
            if (videoPlaying) {
                var bump = document.getElementById('take');
                var canvas = document.getElementById('canvas');
                document.getElementById('canvas').style.margin = '0px';
                document.getElementById('overlay').style.margin = '0px';
                document.getElementById('v').style.margin = '0px';
                document.getElementById('canvas').style.marginLeft = '10px';
                document.getElementById('overlay').style.marginLeft = '10px';
                document.getElementById('v').style.marginLeft = '10px';
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

                document.getElementById('canvas').style.margin = 'auto';
                document.getElementById('overlay').style.margin = 'auto';
                document.getElementById('v').style.margin = 'auto';
            } else {
                localStorage.setItem("backData", imgData);
            }
        }

        function uploadDocs() {
            formdata = new FormData();
            if (formdata) {
                formdata.append("csrfmiddlewaretoken", window.CSRF_TOKEN);
                formdata.append("backImage", localStorage.getItem("backData")); 
                formdata.append("state", state);  
                jQuery.ajax({
                    url: "/onboarding/doc_scan/",
                    type: "POST",
                    data: formdata,
                    processData: false,
                    contentType: false,
                    success: function(data, status, xhttp) {
                        state = "form";
                        if(data.response) {

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
                            //document.getElementById('userData').style.display = "block";
                            document.getElementById('usercontact_form').style.display = "block";
                            document.getElementById('instructions').innerHTML = "Please fill the form with your informations";
                            document.getElementById('photo').setAttribute('src', '');

                            document.forms['usercontact_form']['first_name'].value = user.first_name;
                            document.forms['usercontact_form']['last_name'].value = user.last_name;
                            document.forms['usercontact_form']['nationality'].value = user.nationality;
                            document.forms['usercontact_form']['doe'].value = user.doe;
                            document.forms['usercontact_form']['dob'].value = user.dob;
                            document.forms['usercontact_form']['sex'].value = user.sex;
                            document.forms['usercontact_form']['dni'].value = user.dni;

                        } else if(data.error_msg) {
                            state = "front";
                            document.getElementById('errorHandling').style.display = "block";
                            document.getElementById('errorHandling').innerHTML = data.error_msg;
                            document.getElementById('side').innerHTML = "Please scan the front side of your card";
                            document.getElementById('back_layout').style.display = "none";
                            document.getElementById('front_layout').style.display = "block";
                            document.getElementById('confPicture').style.display = "none";
                            document.getElementById('testPhoto').setAttribute('src', '');
                            document.getElementById('photo').setAttribute('src', '');
                            document.getElementById('take').style.marginTop = "600px";
                            document.getElementById('canvas').style.margin = 'auto';
                            document.getElementById('overlay').style.margin = 'auto';
                            document.getElementById('v').style.margin = 'auto';

                        }
                    }
                 });
            }
        }

        document.getElementById('confDataButton').addEventListener('click',function() {

            var letterNumber = /^[0-9a-zA-Z\s\u00C0-\u017F-]+$/;
            var numbers = /^[0-9]+$/;
            var letters = /^[a-zA-Z\s\u00C0-\u017F-]+$/;
            var first_name = document.forms['usercontact_form']['first_name'].value;
            var last_name = document.forms['usercontact_form']['last_name'].value;
            var nationality = document.forms['usercontact_form']['nationality'].value;
            var dob = document.forms['usercontact_form']['dob'].value;
            var doe = document.forms['usercontact_form']['doe'].value;
            var sex = document.forms['usercontact_form']['sex'].value;
            var dni = document.forms['usercontact_form']['dni'].value;
            if(letters.test(first_name)) {
                document.forms['usercontact_form']['first_name'].style.borderColor = "#0f0";
                if(letters.test(last_name)) {
                    document.forms['usercontact_form']['last_name'].style.borderColor = "#0f0";
                    if(/^[A-Z]{2,4}$/.test(nationality)) {
                        document.forms['usercontact_form']['nationality'].style.borderColor = "#0f0";
                        if(/^\d{4}-\d{2}-\d{2}$/.test(dob)) {
                            document.forms['usercontact_form']['dob'].style.borderColor = "#0f0";
                            if(/^\d{4}-\d{2}-\d{2}$/.test(doe)) {
                                document.forms['usercontact_form']['doe'].style.borderColor = "#0f0";
                                if(sex == 'M' || sex == 'F') {
                                    document.forms['usercontact_form']['sex'].style.borderColor = "#0f0";
                                    if(/^[0-9]{8}[A-Z]{1}$/.test(dni)){
                                        document.forms['usercontact_form']['dni'].style.borderColor = "#0f0";
                                        userDataJson = JSON.stringify({'first_name': first_name, 'last_name': last_name, 'nationality': nationality, 'dob': dob, 'doe': doe, 'sex': sex, 'dni': dni});
                                        formdata = new FormData();
                                        if (formdata) {
                                            formdata.append("csrfmiddlewaretoken", window.CSRF_TOKEN);
                                            formdata.append("frontImage", localStorage.getItem("frontData"));   
                                            formdata.append("backImage", localStorage.getItem("backData")); 
                                            formdata.append("userData", userDataJson);
                                            formdata.append("state", state);  
                                            jQuery.ajax({
                                                url: "/onboarding/doc_scan/",
                                                type: "POST",
                                                data: formdata,
                                                processData: false,
                                                contentType: false,
                                                success: function(data, status, xhttp) {
                                                    window.location = "/onboarding";
                                                },
                                                error: function (request, status, error) {
                                                    console.log(request.responseText);
                                                }
                                            });
                                        }
                                        return true;
                                    }
                                    document.forms['usercontact_form']['dni'].style.borderColor = "#f00";
                                    return false;
                                }
                                document.forms['usercontact_form']['sex'].style.borderColor = "#f00";
                                return false;
                            }
                            document.forms['usercontact_form']['doe'].style.borderColor = "#f00";
                            return false;
                        }
                        document.forms['usercontact_form']['dob'].style.borderColor = "#f00";
                        return false;
                    }
                    document.forms['usercontact_form']['nationality'].style.borderColor = "#f00";
                    return false;
                }
                document.forms['usercontact_form']['last_name'].style.borderColor = "#f00";
                return false;
            }
            document.forms['userData']['first_name'].style.borderColor = "#f00";
            return false;
        });


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