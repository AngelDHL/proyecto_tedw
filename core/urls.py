from django import views
from django.urls import path, include
from core.views import index, category_list_view, product_list_view, category_product_list_view, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart, cart_view, delete_items_from_cart, update_from_cart, checkout_view, payment_completed_view, payment_failed_view, customer_dashboard, order_detail, make_address_default

app_name = "core"

urlpatterns = [
    # Homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    #Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),

    # Vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),

    # Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    # Add review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),

    # Search
    path("search/", search_view, name="search"),
    
    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),

    # Add to cart URL
    path("add-to-cart/", add_to_cart, name="add-to-cart"),

    # Cart page URL
    path("cart/", cart_view, name="cart"),

    # Delete Item Form Cart
    path("delete-from-cart/", delete_items_from_cart, name="delete-from-cart"),

    # Update Cart
    path("update-cart/", update_from_cart, name="update-cart"),

    # Checkout URL
    path("checkout/", checkout_view, name="checkout"),

    # PayPal URL
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Payment Succesful
    path("payment-completed/", payment_completed_view, name="payment-completed"),

    # Payment Failed
    path("payment-failed/", payment_failed_view, name="payment-failed"),

    # Dashboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),

    # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),

    # Making Address Defaulty
    path("make-default-address/", make_address_default, name="make-default-address")
]