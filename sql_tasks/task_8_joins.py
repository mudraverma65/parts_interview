import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    select c.name, (oi.price * oi.quantity) as total 
    from Customers c
    left join Orders o
    on o.customer_id = c.customer_id
    left join Order_Items oi
    on oi.order_id = o.order_id
    group by c.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    conn.close()
    return results
