# Sudarshan IMAX
import math

# Cinema Data
movies = {
    'michael': 'global', 
    'hail mary': 'global', 
    'lik': 'regional', 
    'dacoit': 'regional', 
    'patriot': 'national', 
    'vaazha 2': 'national'
    }
hype_multipiers = {
    'global': 1.05, 
    'continental': 1.03, 
    'national': 1.025, 
    'regional': 1.015
    }
seat_base_price = {
    'marvel': 150, 
    'royal': 200, 
    'executive': 250, 
    'recilenier': 350
    }
timing_multipliers = {
    "afternoon": 1.0,    
    "morning": 1.1,      
    "evening": 1.2,      
    "late_night": 1.3    
}
snack_menu = {
    "1": {"item": "Cheese Popcorn", "price": 180},
    "2": {"item": "Salted Popcorn", "price": 150},
    "3": {"item": "Coca Cola", "price": 90},
    "4": {"item": "Paneer Burger", "price": 120},
    "5": {"item": "Nachos with Salsa", "price": 160}
}
movie_schedule = {
    "michael": {
        "show 1": {"time": "05:45 AM", "screen": "1"},
        "show 2": {"time": "11:15 AM", "screen": "1"},
        "show 3": {"time": "02:45 PM", "screen": "2"},
        "show 4": {"time": "06:45 PM", "screen": "1"}
    },
    "hail mary": {
        "show 1": {"time": "06:00 AM", "screen": "2"},
        "show 2": {"time": "1:30 PM", "screen": "1"},
        "show 3": {"time": "06:15 PM", "screen": "2"},
        "show 4": {"time": "09:15 PM", "screen": "1"}
    },
    "patriot": {
        "show 1": {"time": "08:00 AM", "screen": "1"},
        "show 2": {"time": "11:45 AM", "screen": "3"},
        "show 3": {"time": "05:45 PM", "screen": "3"},
        "show 4": {"time": "12:45 AM", "screen": "1"}
    },
    "vaazha 2": {
        "show 1": {"time": "05:45 AM", "screen": "3"},
        "show 2": {"time": "11:30 AM", "screen": "2"},
        "show 3": {"time": "03:15 PM", "screen": "3"},
        "show 4": {"time": "09:00 PM", "screen": "3"}
    },
    "lik": {
        "show 1": {"time": "08:45 AM", "screen": "2"},
        "show 2": {"time": "05:00 PM", "screen": "2"},
        "show 3": {"time": "09:30 PM", "screen": "2"},
        "show 4": {"time": "12:45 AM", "screen": "2"}
    },
    "dacoit": {
        "show 1": {"time": "09:00 AM", "screen": "3"},
        "show 2": {"time": "03:00 PM", "screen": "3"},
        "show 3": {"time": "06:30 PM", "screen": "3"},
        "show 4": {"time": "12:45 AM", "screen": "3"}
    }
}

# --- FUNCTIONS ---

def movie_selection():
    movie = list(movies)
    print("\n" + "=" * 50)
    print("🎬  NOW SHOWING @ SUDARSHAN IMAX  🎬".center(50))
    print("=" * 50)
    
    # Beautiful list view
    for i, m in enumerate(movie, 1):
        print(f" [{i}] {m.title():<20} | Hype: {movies[m].upper()}")
    
    while True:
        try:
            user_choice = input('\n👉 Which Movie (Name or Number): ').lower().strip()
            if user_choice.isdigit():
                choice = int(user_choice)
                if 1 <= choice <= len(movie):
                    return movie[choice - 1]
                else:
                    print("❌ Please select a number between 1 and", len(movie))
            else:
                if user_choice in movie:
                    return user_choice
                else:
                    print("❌ Movie not found! Please check the list above.")         
        except Exception as e:
            print(f"⚠️ Error: {e}")

def get_show(movie_name):
    shows = movie_schedule[movie_name]
    print(f"\n--- 🕒 Available Shows for: {movie_name.upper()} ---")
    
    for show_num, details in shows.items():
        print(f" ➜ {show_num.title():<10} | {details['time']:<10} | Screen {details['screen']}")
    
    while True:
        choice = input("\n👉 Enter Show Number (1, 2, 3, or 4): ").lower().strip()
        user_show = f"show {choice}"
        if user_show in shows:
            return shows[user_show]
        else:
            print("❌ Invalid show number!")

def get_seat_type():
    print("\n" + "💺 SELECT YOUR COMFORT ".center(50, "─"))
    print("  Marvel (₹150) | Royal (₹200) | Executive (₹300) | Recliner (₹350)")
    
    while True:
        user_choice = input("\n👉 Enter seat type: ").lower().strip()
        if user_choice in seat_base_price:
            return user_choice, seat_base_price[user_choice]
        else:
            print("❌ Invalid seat type! Try: marvel, royal, executive, or recliner")

def get_category_from_time(time_str):
    time_str = time_str.upper()
    if "AM" in time_str: return "morning"
    
    hour = int(time_str.split(":")[0])
    if 1 <= hour <= 4: return "afternoon"
    elif 5 <= hour <= 7: return "evening"
    else: return "night"

def calculate_price(movie_name, show_time, base_price, day):
    hype = movies[movie_name]
    hype_multiplier = hype_multipiers[hype]
    
    if show_time == 'morning': time_multiplier = 1.1
    elif show_time == 'afternoon': time_multiplier = 1.0
    elif show_time == 'evening': time_multiplier = 1.2
    elif show_time == 'night': time_multiplier = 1.3
    else: time_multiplier = 1.0

    weekday = ['saturday', 'sunday']
    day_multiplier = 1.1 if day.lower() in weekday else 1.0
    
    final_price = base_price * time_multiplier * hype_multiplier * day_multiplier
    return round(final_price, 2)

def handle_snacks():
    total_snack_bill = 0.0
    selected_snacks = []

    print("\n" + "🍿 SUDARSHAN FOOD COUNTER ".center(50, "═"))
    for key, val in snack_menu.items():
        print(f"  [{key}] {val['item']:<20} | ₹{val['price']}")
    print("=" * 50)

    while True:
        choice = input("\n👉 Enter item number (or 'n' to finish): ").strip().lower()
        if choice == 'n': break

        if choice in snack_menu:
            item_name = snack_menu[choice]['item']
            item_price = snack_menu[choice]['price']
            total_snack_bill += item_price
            selected_snacks.append(item_name)
            print(f"   ✅ Added {item_name}! Subtotal: ₹{total_snack_bill}")
        else:
            print("   ❌ Invalid item number!")
    
    return total_snack_bill, selected_snacks

def generate_invoice(movie, show, seat, t_price, s_price):
    total = t_price + s_price
    tax = round(total * 0.18)
    final_amt = total + tax

    print("\n" + "★"*45)
    print("      SUDARSHAN IMAX, Bharuch      ".center(45))
    print("★"*45)
    print(f" 🎬 MOVIE      : {movie.upper():<15}")
    print(f" 🕒 SHOW TIME  : {show['time']:<15}")
    print(f" 📺 SCREEN     : {show['screen']:<15}")
    print(f" 💺 SEAT TIER  : {seat.upper():<15}")
    print("-" * 45)
    print(f" 🎫 Ticket Price : ₹{t_price}")
    print(f" 🍿 Snack Bill   : ₹{s_price}")
    print(f" 📝 GST (18%)    : ₹{tax}")
    print("-" * 45)
    print(f" TOTAL PAYABLE : ₹{final_amt}\n".center(45))
    print("★" * 45)
    print("       Thank You! Visit Again       ".center(45))
    print("★" * 45 + "\n")

# The Main screen
def main():
    # Sequence of execution
    selected_movie = movie_selection()
    selected_show = get_show(selected_movie)
    seat_type, b_price = get_seat_type()
    
    day = input("\n📅 Enter Day of Week (e.g. Sunday): ").strip()
    
    time_cat = get_category_from_time(selected_show['time'])
    ticket_price = calculate_price(selected_movie, time_cat, b_price, day)
    
    snack_total, snacks_list = handle_snacks()
    
    generate_invoice(selected_movie, selected_show, seat_type, ticket_price, snack_total)

if __name__ == "__main__":
    main()