document.addEventListener("DOMContentLoaded", function(){
  document.querySelectorAll('.dropdown-submenu .dropdown-toggle').forEach(function(element){
    element.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      let nextEl = this.nextElementSibling;
      if(nextEl && nextEl.classList.contains('dropdown-menu')){
        nextEl.classList.toggle('show');
      }
    });
  })
});

// Excersice
// let a = 4,
//     b = 3,
//     kq = a*b;


// console.log(kq)
// console.log("Ket qua a nhan b la: ")

    

