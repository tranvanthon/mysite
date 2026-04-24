// Tự động thêm class Bootstrap cho các input của Allauth
document.querySelectorAll("input").forEach((input) => {
  if (input.type !== "checkbox") {
    input.classList.add("form-control");
  } else {
    input.classList.add("form-check-input");
  }
});
//menu
document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelectorAll(".dropdown-submenu .dropdown-toggle")
    .forEach(function (element) {
      element.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        let nextEl = this.nextElementSibling;
        if (nextEl && nextEl.classList.contains("dropdown-menu")) {
          nextEl.classList.toggle("show");
        }
      });
    });
});
