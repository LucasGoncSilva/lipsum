window.addEventListener('DOMContentLoaded', function () {
  const title = document.getElementById('id_title')
  const slug_field = document.getElementById('id_slug')


  slug_field.readOnly = true


  function populateSlug() {
    slug_field.value = slugify(title.value)
  }


  title.addEventListener('change', populateSlug)
  title.addEventListener('focus', populateSlug)
  title.addEventListener('keyup', populateSlug)
})