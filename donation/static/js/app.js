document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      if(this.currentStep < 5){
      e.preventDefault();
      }
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});

/* Filtering organizations */

nextButtonOrganizationFiltering = document.getElementById('organization_filter')
nextButtonOrganizationFiltering.addEventListener('click', function (){
  const listOfCategories = createListOfCategories()
  const institutionDivs = document.getElementsByClassName('institution-div')
  for(let i=0; i < institutionDivs.length; i++){
    institutionDivs[i].style.display = 'block'
    const institutionCategories = institutionDivs[i].dataset.categories.split(',')
    for(let j=0; j < listOfCategories.length; j++){
      if(!(institutionCategories.includes(listOfCategories[j]))){
        institutionDivs[i].style.display = 'none'
      }
    }
  }
})


function createListOfCategories() {
  let listOfCategories = []
  const checkboxes = document.querySelectorAll("[name='categories']");
  for(let i=0; i < checkboxes.length; i++){
    if(checkboxes[i].checked === true){
      listOfCategories.push(checkboxes[i].value)
    }
  }
  return listOfCategories
}

/* Creeating Summary */

function createCategoryNamesString() {
  let categoryNamesString = ""
  const categoryDivs = document.getElementsByClassName('category-div')
  // const checkboxes = document.querySelectorAll("[name='categories']");
  for(let i=0; i < categoryDivs.length; i++){
    const checkbox = categoryDivs[i].querySelector("[name='categories']")
    if(checkbox.checked === true){
      const categoryName = categoryDivs[i].getElementsByClassName('category-name')[0].innerText
      categoryNamesString += categoryName + ', '
    }
  }
  return categoryNamesString
}

function createInstitutionName(){
const institutionDivs = document.getElementsByClassName('institution-div')
  for(let i=0; i < institutionDivs.length; i++){
    const checkbox = institutionDivs[i].firstElementChild.querySelector("[name='institution']")
    if(checkbox.checked === true){
      const descriptionSpan = institutionDivs[i].getElementsByClassName('description')[0]
      return descriptionSpan.firstElementChild.innerText

    }
}}

const nextButtonSummary = document.getElementById('summary')
nextButtonSummary.addEventListener('click', function (){
  const bags = document.querySelector("[name='quantity']").value
  const categoryNamesString = createCategoryNamesString()
  const summaryBags = document.getElementById('summary-bags')
  summaryBags.innerText = `${bags} worki ${categoryNamesString}`
  const institutionName = createInstitutionName()
  const summaryInstitution = document.getElementById('summary-institution')
  summaryInstitution.innerText = institutionName
  const summaryStreet = document.getElementById('summary-street')
  const address = document.querySelector("[name='address']").value
  summaryStreet.innerText = address
  const summaryCity = document.getElementById('summary-city')
  const city = document.querySelector("[name='city']").value
  summaryCity.innerText = city
  const summaryZipCode = document.getElementById('summary-zip-code')
  const zipCode = document.querySelector("[name='zip_code']").value
  summaryZipCode.innerText = zipCode
  const summaryPhone = document.getElementById('summary-phone')
  const phone = document.querySelector("[name='phone_number']").value
  summaryPhone.innerText = phone
  const summaryDate = document.getElementById('summary-pick-up-date')
  const date = document.querySelector("[name='pick_up_date']").value
  summaryDate.innerText = date
  const summaryTime = document.getElementById('summary-pick-up-time')
  const time = document.querySelector("[name='pick_up_time']").value
  summaryTime.innerText = time
  const summaryComment = document.getElementById('summary-pick-up-comment')
  const comment = document.querySelector("[name='pick_up_comment']").value
  summaryComment.innerText = comment
})



