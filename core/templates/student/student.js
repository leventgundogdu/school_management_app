document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('login-form');
  var loginButton = document.getElementById('login-button');

  loginButton.addEventListener('click', function (event) {
    event.preventDefault();

    var studentId = document.getElementById('student-id').value;

    var url = "/student/grades/" + studentId + "/";

    window.location.href = url;
  });
});
