# =========================================================
#                     Jinja Bookshop
#                         No 01,
#                     Peterson Road,
#                         US
#                     Phone: +13929209333
#                    Email: jinja@sample.com
#                 Website: samplebookshop.com
# =========================================================

# Bill To:
# {{customer_name}}

# =========================================================
# |    Description     |   Quantity   |   Unit Price   |   Total   |
# =========================================================
# {% for item in items %}
# | {{title}}    |      {{quantity}}   |    {{price}}      | {{total}} |
# {% endfor %}

# =========================================================
# |                                      Subtotal | {{subtotal}}  |
# |                                         Tax   | {{0.1*subtotal}}        |
# |                                   Grand Total   | {{1.2*subtotal}}|
# =========================================================

# Payment Information: {% if payement_method ==  "Cash" %} Cash {%  else %} Credit Card {% endif %}


# Thank you for shopping with us!
# Jinja Bookshop appreciates your business.

# =========================================================


from jinja2 import Environment, FileSystemLoader

enviornment = Environment(loader=FileSystemLoader('templates'))

template = enviornment.get_template('bill_template.txt')

books = [
    {'title': 'The Great Gatsby', 'price': 10},
    {'title': 'The Bell Jar', 'price': 15},
    {'title': 'The Handmaid\'s Tale', 'price': 20}
]

bill_details = [
    {'customer_name': 'John', 'payment_method': 'Cash','book_quantities': [1, 2, 3]},
    {'customer_name': 'Jane', 'payment_method': 'Other', 'book_quantities': [8, 2,7]},
    {'customer_name': 'Joe', 'payment_method': 'Cash', 'book_quantities': [6, 3, 0]}
]

for detail in bill_details:
    with open(f'output/{detail["customer_name"]}.txt', 'w') as f:
        f.write(template.render(
            customer_name=detail['customer_name'],
            payment_method=detail['payment_method'],
            items=[{
                'title': books[i]['title'],
                'quantity': detail['book_quantities'][i],
                'price': books[i]['price'],
                'total': detail['book_quantities'][i] * books[i]['price']
            } for i in range(len(books))],
            subtotal=sum([detail['book_quantities'][i] * books[i]['price'] for i in range(len(books))]),
            payement_method = detail['payment_method']
        ))