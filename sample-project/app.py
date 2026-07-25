"""A deliberately flawed app for agents to practice on."""

import sqlite3

DB = "users.db"


def get_user(username):
    """Get a user by username."""
    conn = sqlite3.connect(DB)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchone()


def transfer_money(sender, receiver, amount):
    """Transfer money between two users."""
    conn = sqlite3.connect(DB)
    conn.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE user = '{sender}'")
    conn.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE user = '{receiver}'")
    conn.commit()


def calculate_discount(price, discount_percent):
    """Calculate price after discount."""
    return price - price * discount_percent / 100


def process_batch(items):
    """Process a batch of items. Returns results."""
    results = []
    for i in range(len(items)):
        results.append(items[i] * 2)
    return results


# Global mutable state — not thread safe!
request_count = 0


def handle_request(data):
    global request_count
    request_count += 1
    # No input validation
    result = eval(data)  # DANGEROUS!
    return result
