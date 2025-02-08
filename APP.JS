let cart = [];
const cartCountElement = document.getElementById('cart-count');
const cartItemsElement = document.getElementById('cart-items');
const totalPriceElement = document.getElementById('total-price');

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        const productElement = button.parentElement;
        const productId = productElement.getAttribute('data-id');
        const productName = productElement.querySelector('h3').innerText;
        const productPrice = parseFloat(productElement.querySelector('p').innerText.replace('Price: $', ''));

        const product = { id: productId, name: productName, price: productPrice };
        cart.push(product);
        updateCart();
    });
});

function updateCart() {
    cartCountElement.innerText = cart.length;
    cartItemsElement.innerHTML = '';
    let total = 0;

    cart.forEach(item => {
        const li = document.createElement('li');
        li.innerText = `${item.name} - $${item.price.toFixed(2)}`;
        cartItemsElement.appendChild(li);
        total += item.price;
    });

    totalPriceElement.innerText = `Total: $${total.toFixed(2)}`;
}