/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

const form = document.querySelector('form');
const address = form.elements['address'];
const btnSubmit = document.querySelector('#submit');
const addressResults = document.getElementById('address-results');
const parseType = document.getElementById('parse-type');
const tableBody = document.querySelector('tbody');

const errorMessage = document.createElement('p');
errorMessage.innerHTML = "Unable to parse this value due to repeated labels.";
errorMessage.style.color = "red";
errorMessage.style.fontWeight = "bold";
errorMessage.style.display = "none";
const parentDiv = form.parentNode;
parentDiv.insertBefore(errorMessage, form);


const getData = (query) => {
   //make sure tableBody is cleared for each new request
   tableBody.innerHTML = "";

   fetch('http://localhost:8000/api/parse/?address=' + query)
      .then(response => {
         return response.json();
      })
      .then(responseData => {
         if ('error' in responseData){
            errorMessage.style.display = "block";
            addressResults.style.display = "none";
         } else {
            errorMessage.style.display = "none";
            let address_components = responseData.address_components; //array with each part in another array as [part, tag]
            let address_type = responseData.address_type; //string
            let input_string = responseData.input_string; //string

            addressResults.style.display = 'block';
            parseType.innerHTML = address_type;
            address_components.forEach(addressPair => {
               //create and append a new tr to the table body
               const newRow = document.createElement('tr');
               newRow.innerHTML = "<td>" + addressPair[0] + "</td><td>" + addressPair[1] + "</td>";
               tableBody.appendChild(newRow);
            });
         }
         
      });
}

form.addEventListener('submit', e => {
   e.preventDefault();
   if (address.value !== "") {
      console.log("the api is getting used");
      let query = encodeURIComponent(address.value);
      getData(query);
   }
})
