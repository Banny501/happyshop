
function add_product_to_cart(url, product_slug){
    if (cart_post_request(url, product_slug)) {
        console.log('adsds');
    }
}

function delete_product_from_cart(url, product_slug){
     if (cart_post_request(url, product_slug)) {
        document.getElementById(product_slug).remove();
    }
}

function cart_post_request(url ,product_slug) {
    return fetch(url, {
              method: 'post',
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken,
              },
              body: 'product=' + product_slug
            })
            .then(response => {
                if (response.ok) {
                    return true;
                }
                else {
                    return false;
                }
              })
            .catch((error) => {
              console.error('Error:', error);
            });
};


