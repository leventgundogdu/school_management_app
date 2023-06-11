// student.js
document.addEventListener('DOMContentLoaded', function () {
  // Get the form and login button elements
  var form = document.getElementById('login-form');
  var loginButton = document.getElementById('login-button');

  // Attach an event listener to the login button
  loginButton.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the student ID from the input field
    var studentId = document.getElementById('student-id').value;

    // Generate the URL with the student ID
    var url = "/student/grades/" + studentId + "/";

    // Redirect to the generated URL
    window.location.href = url;
  });
});
