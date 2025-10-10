// // Viet chuong trinh nhap so nguyen n va in giai thua n!
// let n = Number(prompt("Moi nhap so khong am:"))
// // Kiem tra xem n co phai la khong nguyen, khong am hay khong?
// while (!Number.isInteger(n) || n < 0) {
//     n = Number(prompt("Moi cu nhap lai, chi nhan so nguyen khong am:"));
// }

// // // Tinh giai thua cua n! dung for
// // let gt = 1;

// // for (let i = 1; i <= n; i++) {
// //     gt *= i
// // }
// // alert(`Giai thua cua ${n} la ${gt}`);
// Tinh giai thua cua n! dung while
let i = 1;
let gt =1;

while (i<=n) {
    gt *= i;
    i++;
}
alert(`${n} ! la ${gt}`)
// Bai tap 16: Nhap so a = phim:
// Neu so chan thi tinh tong tu 0 den a. Neu so le dua message:"Toi 0 tinh tong le, byebye" va thoat

// let a = Number(prompt("Moi nhap so:"));

// for (let i = 0; !Number.isInteger(a); i++) {
//     if (i%2 !== 0) {
//         i += i;
//         break;
//     } else {
//         alert("Xin loi toi 0 tinh tong le, byebye!");
//         break;
//     }
// }
// alert("Tong cac so le tu", 0, "den", a, "la", i)