window.addEventListener('DOMContentLoaded', function () {
  const thirdyPartyLoginDiv = document.getElementById('div_id_thirdy_party_login_name')
  const thirdyPartyLogin = document.getElementById('id_thirdy_party_login_name')
  const loginDiv = document.getElementById('div_id_login')
  const login = document.getElementById('id_login')
  const passwordDiv = document.getElementById('div_id_password')
  const password = document.getElementById('id_password')
  const thirdyPartyCheck = document.getElementById('id_thirdy_party_login')
  const form = document.querySelector('form')
  const service = document.getElementById('id_service')
  const name = document.getElementById('id_name')
  const slug_field = document.getElementById('id_slug')


  slug_field.readOnly = true


  if (thirdyPartyCheck.checked) {
    login.value = '-----'
    password.value = '-----'
    loginDiv.classList.add('hide')
    passwordDiv.classList.add('hide')
  } else {
    thirdyPartyLogin.value = '-----'
    thirdyPartyLoginDiv.classList.add('hide')
  }


  function toggleFields() {
    thirdyPartyLoginDiv.classList.toggle('hide')
    loginDiv.classList.toggle('hide')
    passwordDiv.classList.toggle('hide')
  }


  function populateSlug() {
    slug_field.value = service.value + slugify(name.value)
  }


  thirdyPartyCheck.onclick = function () {
    if (this.checked) {
      login.value = '-----'
      password.value = '-----'
      toggleFields()
      thirdyPartyLogin.value = ''
    } else {
      thirdyPartyLogin.value = '-----'
      toggleFields()
      login.value = ''
      password.value = ''
    }
  }

  form.onsubmit = function () {
    if (!thirdyPartyCheck.checked) {
      thirdyPartyLogin.value = '-----'
    } else {
      login.value = '-----'
      password.value = '-----'
    }
  }

  service.addEventListener('change', populateSlug)
  service.addEventListener('focus', populateSlug)
  service.addEventListener('keyup', populateSlug)
  name.addEventListener('change', populateSlug)
  name.addEventListener('focus', populateSlug)
  name.addEventListener('keyup', populateSlug)
})