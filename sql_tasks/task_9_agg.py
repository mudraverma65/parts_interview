import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    select oi.sku, SUM(oi.quantity) as total_quantity from Order_items oi
    join Orders o
    on o.order_id = oi.order_id
    group by oi.sku having total_quantity > 1
    """
    
    results = cursor.execute(query)
    return cursor.fetchall()