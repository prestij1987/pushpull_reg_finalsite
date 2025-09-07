



// собираем данные из формы

function serializeForm(formNode) {
    console.log(formNode.elements)
  }
  
  function handleFormSubmit(event) {
    event.preventDefault()
    serializeForm(applicantForm)
  }
  
  const applicantForm = document.getElementById('zapros_form')
  applicantForm.addEventListener('submit', handleFormSubmit)


  function serializeForm(formNode) {
    const { elements } = formNode
  
    Array.from(elements)
      .forEach((element) => {
        const { name, value } = element
        console.log({ name, value })
      })
  }

  function serializeForm(formNode) {
    const { elements } = formNode
    const data = Array.from(elements)
      .filter((item) => !!item.name)
      .map((element) => {
        const { name, value } = element
  
        return { name, value }}
      

var number = '';
var name = '';        

