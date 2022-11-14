/* global bootstrap: false */
(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
        new bootstrap.Tooltip(tooltipTriggerEl)
    })
})()

function logoutRegister(url) {
    $(".logout").on("click", e => {
        if (confirm("Siz haqiqatdan ham chiqishni tasdiqlaysizmi?")) {
            location.href = url;
        }
    });
};

function request(config, success) {
    let interval;
    interval = setInterval(() => {
        $.ajax(config).always((data, statusCode, jqXHR) => {
            if (jqXHR.status == 200) {
                clearInterval(interval);
                success(data);
            }
        })
    }, 100);
}
