function postForm() {
    $("#form").validate({
        rules: {
            nom: {
                required: true,
                minlength: 3
            },
            prenom: {
                required: true,
                minlength: 3
            },
            mail: {
                required: true,
                email: true
            },
            bday: {
                required: true,
                date: true
            }
        }
    })
    alert(form["nom"].value + " " + form["prenom"].value + " " + form["bday"].value + " " + form["comment"].value + " " + form["mail"].value);
    document.forms["form"].submit();
    return false;
}

function clearzone() {
    area = document.getElementById("comment");
    area.innerHTML = '';
}