# test
def sort_groceries_auto():
    """
    A Python program that helps you sort your groceries into categories,
    with an automatic sorting feature based on keywords.
    """
    # Define common grocery categories and associated keywords/items.
    # The order of categories here can influence which category an item
    # is placed into if it matches keywords from multiple categories
    # (e.g., "milk" could be Dairy or Beverage; the first category in this
    # dictionary that contains a matching keyword will "win").
    # All keywords are lowercase for case-insensitive matching.
    category_keywords = {
        "Fruits": [
            "apple",
            "banana",
            "orange",
            "grape",
            "strawberry",
            "blueberry",
            "raspberry",
            "lemon",
            "lime",
            "peach",
            "pear",
            "mango",
            "pineapple",
            "kiwi",
            "melon",
            "cherry",
            "avocado",
            "plum",
            "fig",
            "apricot",
            "cranberry",
            "date",
            "pomegranate",
        ],
        "Vegetables": [
            "carrot",
            "broccoli",
            "spinach",
            "lettuce",
            "tomato",
            "cucumber",
            "onion",
            "garlic",
            "potato",
            "sweet potato",
            "bell pepper",
            "zucchini",
            "eggplant",
            "cabbage",
            "kale",
            "celery",
            "mushroom",
            "corn",
            "peas",
            "green bean",
            "asparagus",
            "brussels sprout",
            "cauliflower",
            "squash",
            "ginger",
            "chili",
            "jalapeno",
            "artichoke",
            "radish",
            "beet",
            "leek",
            "bok choy",
        ],
        "Dairy & Eggs": [
            "milk",
            "cheese",
            "yogurt",
            "butter",
            "egg",
            "cream",
            "sour cream",
            "cottage cheese",
            "cream cheese",
            "ghee",
            "kefir",
            "creamer",
            "margarine",
            "feta",
            "cheddar",
            "mozzarella",
            "Quark",
        ],
        "Meat & Seafood": [
            "chicken",
            "beef",
            "sausage",
            "ham",
            "turkey",
            "fish",
            "salmon",
            "tuna",
            "shrimp",
            "crab",
            "scallop",
            "lamb",
            "steak",
            "ground beef",
            "hot dog",
            "salami",
            "pepperoni",
            "cod",
            "tilapia",
            "oyster",
            "clams",
        ],
        "Pantry Items": [
            "pasta",
            "rice",
            "flour",
            "sugar",
            "salt",
            "pepper",
            "oil",
            "vinegar",
            "canned",
            "soup",
            "sauce",
            "cereal",
            "oats",
            "tortilla",
            "coffee",
            "tea",
            "jam",
            "honey",
            "spices",
            "nuts",
            "beans",
            "lentils",
            "broth",
            "syrup",
            "baking soda",
            "baking powder",
            "ketchup",
            "mustard",
            "mayonnaise",
            "crackers",
            "granola",
            "dried fruit",
            "peanut butter",
            "almond butter",
            "soy sauce",
            "olive oil",
            "vegetable oil",
            "quinoa",
            "couscous",
            "brownie mix",
            "cake mix",
            "chocolate chips",
            "gelatin",
            "cornstarch",
            "yeast",
            "olives",
            "pickles",
            "chips",
            "cookies",
            "salsa",  # Some overlap with snacks, but often stored in pantry
        ],
        "Frozen Foods": [
            "ice cream",
            "frozen pizza",
            "frozen vegetable",
            "frozen fruit",
            "frozen meal",
            "waffle",
            "fries",
            "tater tot",
            "burrito",
            "nuggets",
            "fish sticks",
            "hash brown",
            "popsicle",
            "sorbet",
            "ice",
            "dough",
            "smoothie mix",
        ],
        "Beverages": [
            "juice",
            "soda",
            "water",
            "beer",
            "wine",
            "cola",
            "sparkling water",
            "tea bag",
            "coffee grounds",
            "energy drink",
            "sports drink",
            "liquer",
            "seltzer",
            "kombucha",
            "almond milk",
            "soy milk",
            "oat milk",
        ],
        "Snacks": [
            "chips",
            "cookie",
            "cracker",
            "bar",
            "candy",
            "chocolate",
            "popcorn",
            "pretzels",
            "nuts",
            "granola bar",
            "fruit snack",
            "gummy",
            "jerky",
            "trail mix",
            "rice cakes",
            "wafers",
        ],
        "Bakery": [
            "bread",
            "bagel",
            "muffin",
            "croissant",
            "donut",
            "pastry",
            "pie",
            "cupcake",
            "sourdough",
            "rolls",
            "buns",
            "tarts",
            "bread",
        ],
        "Household & Personal Care": [
            "soap",
            "shampoo",
            "conditioner",
            "toothpaste",
            "brush",
            "detergent",
            "cleaner",
            "toilet paper",
            "paper towel",
            "sponge",
            "lotion",
            "razor",
            "tissue",
            "trash bag",
            "dish soap",
            "hand soap",
            "deodorant",
            "mouthwash",
            "laundry",
            "fabric softener",
            "bleach",
            "disinfectant",
            "air freshener",
            "light bulb",
            "battery",
            "aluminum foil",
            "plastic wrap",
            "ziploc",
            "band-aid",
            "medicine",
            "vitamins",
            "shaving cream",
        ],
        "Other": [],  # Items that don't fit above, or for manual assignment
    }

    # Initialize sorted_groceries with all categories, but empty lists
    # This ensures all categories are present in the final output, even if empty
    sorted_groceries = {category: [] for category in category_keywords}

    print("=" * 40)
    print(" Welcome to your Smart Grocery Sorter! ")
    print("=" * 40)
    print("Enter your grocery items one by one. Type 'done' when you're finished.")
    print("The program will try to automatically sort items based on keywords.")
    print("If it can't find a match, you'll be asked to choose a category manually.")
    print("-" * 40)

    # Display available categories for manual selection (if needed)
    category_names_for_manual_selection = list(category_keywords.keys())
    print("Available categories for manual sorting (if needed):")
    for i, cat in enumerate(category_names_for_manual_selection):
        print(f"  {i + 1}. {cat}")
    print("-" * 40)

    while True:
        item_input = input("Enter grocery item (or 'done' to finish): ").strip()

        if item_input.lower() == "done":
            break
        if not item_input:  # Handle empty input for item name
            print("Please enter an item name.")
            continue

        item_normalized = item_input.lower()
        assigned_automatically = False

        # Attempt automatic sorting
        # We iterate through categories, and for each category, check if any of its
        # keywords are present in the entered item name.
        for category, keywords in category_keywords.items():
            # The 'if keyword' ensures we don't try to match against an empty string keyword
            if any(keyword in item_normalized for keyword in keywords if keyword):
                sorted_groceries[category].append(item_input)
                print(f"'{item_input}' automatically added to '{category}'.")
                assigned_automatically = True
                break  # Item found and assigned, move to the next grocery input

        # If no automatic match was found, ask the user to choose a category
        if not assigned_automatically:
            category_names_for_manual_selection = list(category_keywords.keys())
            print("Available categories for manual sorting (if needed):")
            for i, cat in enumerate(category_names_for_manual_selection):
                print(f"  {i + 1}. {cat}")
            print("-" * 40)
            print(
                f"Could not automatically sort '{item_input}'. Please choose a category:"
            )

            while True:
                category_choice = input(
                    f"Which category does '{item_input}' belong to? (Enter number or category name): "
                ).strip()

                chosen_category = None

                # Try to match by number
                if category_choice.isdigit():
                    idx = int(category_choice) - 1
                    if 0 <= idx < len(category_names_for_manual_selection):
                        chosen_category = category_names_for_manual_selection[idx]
                else:
                    # Try to match by category name (case-insensitive)
                    for cat_name in category_names_for_manual_selection:
                        if category_choice.lower() == cat_name.lower():
                            chosen_category = cat_name
                            break

                if chosen_category:
                    sorted_groceries[chosen_category].append(item_input)
                    print(f"'{item_input}' manually added to '{chosen_category}'.")
                    break  # Exit inner loop, go to next item
                else:
                    print(
                        "Invalid category choice. Please enter a valid number or category name from the list."
                    )

    print("" + "=" * 40)
    print(" Your Sorted Groceries: ")
    print("=" * 40)

    # Display the sorted groceries
    found_items = False
    for category, items in sorted_groceries.items():
        if items:  # Only print categories that have items
            found_items = True
            print(f"--- {category} ---")
            for item in items:
                print(f"- {item}")

    if not found_items:
        print("No items were entered or sorted.")

    print("" + "=" * 40)
    print(" Happy organizing! ")
    print("=" * 40)


# Run the program when the script is executed
if __name__ == "__main__":
    sort_groceries_auto()
