// Invoke Functions Call on Document Loaded

// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });


// let alertWrapper = document.querySelectorAll('.alert')
// let alertClose = document.querySelectorAll('.alert__close')

// if (alertWrapper) {
//   alertClose.addEventListener('click', () =>
//     alertWrapper.style.display = 'none'
//   )
// }


// document.addEventListener('DOMContentLoaded', function () {
//   // Highlight JS initialization (if needed)
//   hljs.highlightAll();

//   // Select all alert wrappers and their close buttons
//   let alertWrappers = document.querySelectorAll('.alert');
//   let alertCloses = document.querySelectorAll('.alert__close');
  
//   if (alertWrapper) {
//     alertClose.addEventListener('click', () =>
//       alertWrapper.style.display = 'none'
//   });

document.addEventListener('DOMContentLoaded', function () {
  // Initialize syntax highlighting
  hljs.highlightAll();

  let alertWrappers = document.querySelectorAll('.alert'); // Select all alerts
  let alertCloses = document.querySelectorAll('.alert__close'); // Select all close buttons

  // Loop through each close button
  alertCloses.forEach((alertClose, index) => {
    alertClose.addEventListener('click', () => {
      // Hide the corresponding alert
      if (alertWrappers[index]) {
        alertWrappers[index].style.display = 'none';
      }
    });
  });
});
