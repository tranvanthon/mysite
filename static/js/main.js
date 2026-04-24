// Tự động thêm class Bootstrap cho các input của Allauth
document.querySelectorAll("input").forEach((input) => {
  if (input.type !== "checkbox") {
    input.classList.add("form-control");
  } else {
    input.classList.add("form-check-input");
  }
});
//menu
// menu.js - Có hiệu ứng
document.addEventListener("DOMContentLoaded", function () {
  // Xử lý dropdown cấp 1 hover
  var verticalDropdown = document.querySelector(".navbar-vertical.dropdown");
  if (verticalDropdown) {
    var dropdownMenu = verticalDropdown.querySelector(".dropdown-menu");

    verticalDropdown.addEventListener("mouseenter", function () {
      var menu = this.querySelector(".dropdown-menu");
      if (menu) {
        menu.classList.add("show");
        // Thêm class để trigger animation
        menu.style.display = "block";
        setTimeout(() => {
          menu.style.opacity = "1";
          menu.style.transform = "translateY(0)";
        }, 10);
      }
    });

    verticalDropdown.addEventListener("mouseleave", function () {
      var menu = this.querySelector(".dropdown-menu");
      if (menu) {
        menu.classList.remove("show");
        menu.style.opacity = "0";
        menu.style.transform = "translateY(-10px)";
        setTimeout(() => {
          if (!menu.classList.contains("show")) {
            menu.style.display = "none";
          }
        }, 300);
      }
    });
  }

  // Xử lý submenu cấp 2 hover - Có hiệu ứng
  var submenus = document.querySelectorAll(".dropdown-submenu");

  submenus.forEach(function (submenu) {
    var timeoutId; // Để delay khi rời chuột

    submenu.addEventListener("mouseenter", function (e) {
      clearTimeout(timeoutId); // Xóa timeout nếu có
      var submenuList = this.querySelector(".dropdown-menu");
      if (submenuList) {
        // Đóng các submenu khác
        submenus.forEach(function (other) {
          var otherMenu = other.querySelector(".dropdown-menu");
          if (otherMenu && otherMenu !== submenuList) {
            otherMenu.classList.remove("show");
            otherMenu.style.opacity = "0";
            otherMenu.style.transform = "translateX(-10px)";
            setTimeout(() => {
              if (!otherMenu.classList.contains("show")) {
                otherMenu.style.display = "none";
              }
            }, 200);
          }
        });

        // Hiển thị submenu với hiệu ứng
        submenuList.style.display = "block";
        setTimeout(() => {
          submenuList.classList.add("show");
          submenuList.style.opacity = "1";
          submenuList.style.transform = "translateX(0)";
        }, 10);
      }
    });

    submenu.addEventListener("mouseleave", function (e) {
      var submenuList = this.querySelector(".dropdown-menu");
      if (submenuList) {
        // Delay ẩn để tránh mất submenu khi di chuột qua
        timeoutId = setTimeout(() => {
          submenuList.classList.remove("show");
          submenuList.style.opacity = "0";
          submenuList.style.transform = "translateX(-10px)";
          setTimeout(() => {
            if (!submenuList.classList.contains("show")) {
              submenuList.style.display = "none";
            }
          }, 200);
        }, 100);
      }
    });

    // Khi chuột vào submenu thì clear timeout
    var submenuList = submenu.querySelector(".dropdown-menu");
    if (submenuList) {
      submenuList.addEventListener("mouseenter", function () {
        clearTimeout(timeoutId);
      });

      submenuList.addEventListener("mouseleave", function () {
        timeoutId = setTimeout(() => {
          submenuList.classList.remove("show");
          submenuList.style.opacity = "0";
          submenuList.style.transform = "translateX(-10px)";
          setTimeout(() => {
            if (!submenuList.classList.contains("show")) {
              submenuList.style.display = "none";
            }
          }, 200);
        }, 100);
      });
    }
  });
});
