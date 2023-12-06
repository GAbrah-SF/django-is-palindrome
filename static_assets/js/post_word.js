function sendWord() {
    let data = {
        "palabra": this.dataForm.inputWord,
        'X-CSRFToken': this.csrfToken
    }

    $.ajax({
        url: this.url_relative_guardar,
        type: "POST",
        data: data,
        success: function (success) {
            swal.fire({
                position: 'center',
                icon: success.icon,
                background: "#000",
                title: success.message,
                showConfirmButton: false,
                timer: 2500
            })
        },
        error: function (error) {
            swal.fire({
                position: 'center',
                icon: error.responseJSON.icon,
                background: "#000",
                title: error.responseJSON.message,
                showConfirmButton: false,
                timer: 2500
            })
        }
    })
}
