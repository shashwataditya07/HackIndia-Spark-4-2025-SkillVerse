// Sample product data
const products = [
  {
    id: 1,
    name: "Heart",
    description: "Pumps oxygenated blood throughout the body.",
    image: "images/medicine1.jpg",
  },
  {
    id: 2,
    name: "Lungs",
    description: "Responsible for breathing and gas exchange.",
    image: "images/medicine2.jpg",
  },
  {
    id: 3,
    name: "Liver",
    description: "Detoxifies harmful substances.",
    image: "images/medicine1.jpg",
  },
  {
    id: 4,
    name: "Kidneys",
    description: "Filters waste from the blood.",
    image: "images/medicine2.jpg",
  },
];
// Load products dynamically into the product list
const loadProducts = () => {
  const productList = document.getElementById("product-list");
  products.forEach((product) => {
    const productCard = `
      <div class="product-card">
        <img src="${product.image}" alt="${product.name}" />
        <h3>${product.name}</h3>
        <p>${product.description}</p>
        <button onclick="addToCart(${product.id})">Add to Cart</button>
      </div>
    `;
    productList.innerHTML += productCard;
  });
};

// Add product to cart (simulated action)
//const addToCart = (productId) => {
 // const product = products.find((p) => p.id === productId);
  //alert(${product.name} has been added to your cart!);
//};

// Load products on page load
document.addEventListener("DOMContentLoaded", loadProducts);

// Handle organ donation form submission
document.getElementById("donation-form").addEventListener("submit", (event) => {
  event.preventDefault();

  // Get user input values
  const fullName = document.getElementById("fullName").value.trim;
  const email = document.getElementById("email").value.trim;
  const selectedOrgans = Array.from(
    document.getElementById("organs").selectedOptions
  ).map((option) => option.value);


  // Validate input
  if (!fullName || !email || selectedOrgans.length === 0) {
    showResult("⚠ Please fill in all fields and select at least one organ.", "error");
    return;
  }

  // Create data object
  const formData = { fullName, email, organs: selectedOrgans };

  // Send data to backend
  fetch("http://localhost:5000/api/donations/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  })
    .then(response => response.json())
    .then(result => {
      if (result.success) {
        showResult(`✅ Thank you, <strong>${fullName}</strong>! You have successfully registered to donate: <strong>${selectedOrgans.join(", ")}</strong>.`, "success");
        document.getElementById("donation-form").reset();
      } else {
        showResult(`❌ Registration failed: ${result.message}`, "error");
      }
    })
    .catch(() => showResult("❌ Server error. Please try again later.", "error"));
});

// Show result message
function showResult(message, type) {
  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = `<p class="${type}">${message}</p>`;
  resultDiv.style.display = "block";
}
//   // Display result to the user
//   if (selectedOrgans.length > 0) {
//     document.getElementById(
//       "result"
//     ).innerHTML = `<p>Thank you, <strong>${fullName}</strong>! You have successfully registered to donate: <strong>${selectedOrgans.join(
//       ", "
//     )}</strong>.</p>`;
//   } else {
//     document.getElementById(
//       "result"
//     ).innerHTML = <p>Please select at least one organ to donate.</p>;
//   }

//   // Optional: Clear form after submission
//   document.getElementById("donation-form").reset();
// });



// // Handle organ donation form submission
// document.getElementById("donation-form").addEventListener("submit", (event) => {
//   event.preventDefault();

//   // Get user input values
//   const fullName = document.getElementById("fullName").value.trim();
//   const email = document.getElementById("email").value.trim();
//   const selectedOrgans = Array.from(
//     document.getElementById("organs").selectedOptions
//   ).map((option) => option.text);

//   // Validate input
//   if (fullName === "" || email === "" || selectedOrgans.length === 0) {
//     showResult("⚠ Please fill in all fields and select at least one organ.", "error");
//     return;
//   }

//   // Display success message
//   showResult(
//     `✅ Thank you, <strong>${fullName}</strong>! You have successfully registered to donate: <strong>${selectedOrgans.join(
//       ", "
//     )}</strong>.`,
//     "success"
//   );

//   // Optional: Clear form after submission
//   document.getElementById("donation-form").reset();
// });

// // Show result message
// function showResult(message, type) {
//   const resultDiv = document.getElementById("result");
//   resultDiv.innerHTML = <p class="${type}">${message}</p>;
//   resultDiv.style.display = "block";
// }