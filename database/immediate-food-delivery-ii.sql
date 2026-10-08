# Write your MySQL query statement below
with first_orders as (
    select 
        customer_id, 
        delivery_id,
        order_date,
        customer_pref_delivery_date,
        row_number() over (
            partition by customer_id
            order by order_date
        ) as rn
    from delivery
)

select 
    round(avg(order_date=customer_pref_delivery_date)*100,2) as immediate_percentage
from first_orders
where rn=1;
