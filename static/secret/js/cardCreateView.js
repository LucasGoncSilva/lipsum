window.addEventListener('DOMContentLoaded', function () {
  const bank = document.getElementById('id_bank')
  const name = document.getElementById('id_name')
  const slug_field = document.getElementById('id_slug')


  slug_field.readOnly = true


  function populateSlug() {
    slug_field.value = bank.value + slugify(name.value)
  }


  bank.addEventListener('change', populateSlug)
  bank.addEventListener('focus', populateSlug)
  bank.addEventListener('keyup', populateSlug)
  name.addEventListener('change', populateSlug)
  name.addEventListener('focus', populateSlug)
  name.addEventListener('keyup', populateSlug)
})