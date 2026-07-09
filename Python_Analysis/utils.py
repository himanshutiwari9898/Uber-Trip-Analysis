# utils.py

def format_currency(value):
    return f"₹{value:,.2f}"

def format_number(value):
    return f"{value:,}"

def format_percentage(value):
    return f"{value:.2f}%"