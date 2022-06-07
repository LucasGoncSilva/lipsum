window.addEventListener('DOMContentLoaded', function () {
  const thirdyPartyLoginDiv = document.getElementById('div_id_thirdy_party_login_name')
  const thirdyPartyLogin = document.getElementById('id_thirdy_party_login_name')
  const loginDiv = document.getElementById('div_id_login')
  const login = document.getElementById('id_login')
  const passwordDiv = document.getElementById('div_id_password')
  const password = document.getElementById('id_password')
  const thirdyPartyCheck = document.getElementById('id_thirdy_party_login')
  const form = document.querySelector('form')


  if (thirdyPartyCheck.checked === true) {
    login.value = ''
    password.value = ''
    loginDiv.classList.add('hide')
    passwordDiv.classList.add('hide')
  } else {
    thirdyPartyLogin.value = ''
    thirdyPartyLoginDiv.classList.add('hide')
  }


  function toggleFields() {
    thirdyPartyLoginDiv.classList.toggle('hide')
    loginDiv.classList.toggle('hide')
    passwordDiv.classList.toggle('hide')
  }


  thirdyPartyCheck.onclick = function () {
    if (this.checked) {
      login.value = '-----'
      password.value = '-----'
      thirdyPartyLogin.value = ''
      toggleFields()
    } else {
      thirdyPartyLogin.value = '-----'
      toggleFields()
      login.value = ''
      password.value = ''
    }
  }

  form.onsubmit = function () {
    if (thirdyPartyCheck.checked) {
      login.value = '-----'
      password.value = '-----'
    } else {
      thirdyPartyLogin.value = '-----'
    }
  }
})