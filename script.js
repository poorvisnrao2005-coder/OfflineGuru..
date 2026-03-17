function showLogin(type){

document.getElementById("student").classList.add("hidden");
document.getElementById("teacher").classList.add("hidden");

document.getElementById(type).classList.remove("hidden");

}

function studentLogin(){

let id = document.getElementById("studentId").value;
let password = document.getElementById("studentPassword").value;

if(id === "" || password === ""){
	alert("Please fill all fields");
	return;
}

window.location.href = "student-dashboard.html";

}

function teacherLogin(){

let id = document.getElementById("teacherId").value;
let password = document.getElementById("teacherPassword").value;

if(id === "" || password === ""){
	alert("Please fill all fields");
	return;
}

window.location.href = "teacher-dashboard.html";

}